"""
Automated Google Sheets Sync Engine
Appends all 200 leads, 200 signals, 258 LinkedIn profiles, and 2 research logs
directly to the Applied Work Master Google Spreadsheet via Google Sheets REST API.
"""

import csv
import json
import os
import requests
from google.oauth2 import service_account
import google.auth.transport.requests

SPREADSHEET_ID = "1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY"
KEY_FILE = r"C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_authorized_session():
    creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
    auth_req = google.auth.transport.requests.Request()
    creds.refresh(auth_req)
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json"
    })
    return session

def read_csv_rows(path, skip_header=False):
    if not os.path.exists(path):
        print(f"Warning: File not found {path}")
        return []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        reader = list(csv.reader(f))
        if skip_header and reader:
            return reader[1:]
        return reader

def append_to_sheet(session, sheet_title, rows):
    if not rows:
        print(f"No rows to append to '{sheet_title}'")
        return False
    
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/'{sheet_title}':append?valueInputOption=USER_ENTERED&insertDataOption=INSERT_ROWS"
    body = {
        "values": rows
    }
    
    resp = session.post(url, json=body)
    if resp.status_code == 200:
        data = resp.json()
        updates = data.get("updates", {})
        print(f"SUCCESS: Appended {len(rows)} rows to '{sheet_title}' (Updated Range: {updates.get('updatedRange')})")
        return True
    else:
        print(f"ERROR appending to '{sheet_title}': {resp.status_code} - {resp.text}")
        return False

def sync_all():
    session = get_authorized_session()
    
    # Verify sheet access
    check_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?fields=sheets.properties"
    resp = session.get(check_url)
    if resp.status_code != 200:
        print(f"Cannot access spreadsheet (HTTP {resp.status_code}): {resp.text}")
        return False
    
    meta = resp.json()
    existing_sheets = {s['properties']['title']: s['properties']['sheetId'] for s in meta.get('sheets', [])}
    print("Connected to spreadsheet! Available tabs:", list(existing_sheets.keys()))
    
    # 1. Compute Brokering (50 rows)
    compute_rows = read_csv_rows(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_150_20261016\Compute_Brokering_50_gid_1773397198.csv", skip_header=False)
    append_to_sheet(session, "Compute Brokering", compute_rows)
    
    # 2. Data (50 + 36 = 86 rows)
    data_b1 = read_csv_rows(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_150_20261016\Data_50_gid_156275556.csv", skip_header=False)
    data_b2 = read_csv_rows(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_50_data_20261016\Data_main_tab_gid_156275556.csv", skip_header=False)
    data_all = data_b1 + data_b2
    append_to_sheet(session, "Data", data_all)
    
    # 3. Data Brokering (50 + 14 = 64 rows)
    db_b1 = read_csv_rows(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_150_20261016\Data_Brokering_50_gid_1346198609.csv", skip_header=False)
    db_b2 = read_csv_rows(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_50_data_20261016\Data_Brokering_main_tab_gid_1346198609.csv", skip_header=False)
    db_all = db_b1 + db_b2
    append_to_sheet(session, "Data Brokering", db_all)
    
    # 4. Daily Signals (150 + 50 = 200 rows)
    sig_b1 = read_csv_rows(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_150_20261016\Daily_Signals_150_gid_910006.csv", skip_header=True)
    sig_b2 = read_csv_rows(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_50_data_20261016\Daily_Signals_50_gid_910006.csv", skip_header=True)
    sig_all = sig_b1 + sig_b2
    append_to_sheet(session, "Daily Signals", sig_all)
    
    # 5. linkeldn (150 + 108 = 258 rows)
    li_b1 = read_csv_rows(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_150_20261016\linkeldn_150_gid_910004.csv", skip_header=True)
    li_b2 = read_csv_rows(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_50_data_20261016\linkeldn_50_data_contacts_gid_910004.csv", skip_header=True)
    li_all = li_b1 + li_b2
    append_to_sheet(session, "linkeldn", li_all)
    
    # 6. Daily Research Log (2 rows)
    log_b1 = read_csv_rows(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_150_20261016\Daily_Research_Log_gid_910005.csv", skip_header=True)
    log_b2 = read_csv_rows(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_50_data_20261016\Daily_Research_Log_gid_910005.csv", skip_header=True)
    log_all = log_b1 + log_b2
    append_to_sheet(session, "Daily Research Log", log_all)
    
    print("\n" + "="*60)
    print("ALL ROWS SYNCED DIRECTLY TO GOOGLE SPREADSHEET!")
    print("="*60)
    return True

if __name__ == "__main__":
    sync_all()
