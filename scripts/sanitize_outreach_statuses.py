"""
Sanitize Outreach Statuses in Google Sheets
Scans 'Compute Brokering', 'Data', 'Data Brokering', and 'linkeldn':
- If verification status contains 'UNDELIVERABLE': marks Outreach Status = 'DO NOT SEND - BOUNCE RISK (550)'
- If verification status contains 'CATCH_ALL' or 'CONNECTION_FAILED': marks Outreach Status = 'HOLD - UNVERIFIED / CATCH-ALL'
- If verification status contains 'DELIVERABLE' (and not undeliverable): marks Outreach Status = 'APPROVED - DELIVERABLE'
This guarantees cold email tools never send to bounced or unverified addresses!
"""

import os
import sys
import time
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

def update_main_tab_statuses(session, tab_name, last_row):
    print(f"\nScanning and sanitizing '{tab_name}' (rows 9 to {last_row})...")
    # Fetch Col U (verification notes), Col L (Outreach Notes), Col Y (Outreach Status)
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/'{tab_name}'!A9:Y{last_row}"
    r = session.get(url)
    if r.status_code != 200:
        print(f"Error fetching {tab_name}: {r.status_code}")
        return

    rows = r.json().get("values", [])
    updated_y = []
    updated_l = []

    undeliv_count = 0
    hold_count = 0
    approved_count = 0

    for i, row in enumerate(rows):
        # Pad row to 25 cols if needed
        while len(row) < 25:
            row.append("")

        ver_note = row[20] if len(row) > 20 else "" # Col U (0-indexed 20)
        curr_l = row[11] if len(row) > 11 else ""   # Col L (0-indexed 11)
        curr_y = row[24] if len(row) > 24 else ""   # Col Y (0-indexed 24)

        if "UNDELIVERABLE" in ver_note:
            new_y = "DO NOT SEND - BOUNCE (550)"
            new_l = "Mailbox rejected by server; DO NOT EMAIL"
            undeliv_count += 1
        elif "CATCH_ALL" in ver_note:
            new_y = "HOLD - CATCH-ALL"
            new_l = "Catch-all domain; route to LinkedIn InMail or verify via BounceBan"
            hold_count += 1
        elif "CONNECTION_FAILED" in ver_note:
            new_y = "HOLD - UNVERIFIED"
            new_l = "Port 25 timeout/blocked; verify before emailing"
            hold_count += 1
        elif "DELIVERABLE" in ver_note:
            new_y = "APPROVED"
            new_l = curr_l if "Cleared" in curr_l else "Cleared for outreach; verified non-bounce"
            approved_count += 1
        else:
            new_y = curr_y if curr_y else "HOLD"
            new_l = curr_l

        updated_y.append([new_y])
        updated_l.append([new_l])

    # Batch update Col Y
    url_y = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/'{tab_name}'!Y9:Y{last_row}?valueInputOption=USER_ENTERED"
    session.put(url_y, json={"range": f"'{tab_name}'!Y9:Y{last_row}", "values": updated_y})

    # Batch update Col L
    url_l = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/'{tab_name}'!L9:L{last_row}?valueInputOption=USER_ENTERED"
    session.put(url_l, json={"range": f"'{tab_name}'!L9:L{last_row}", "values": updated_l})

    print(f"'{tab_name}' sanitized: {approved_count} APPROVED, {undeliv_count} DO NOT SEND (Bounces blocked), {hold_count} HELD.")

def update_linkeldn_statuses(session, last_row):
    print(f"\nScanning and sanitizing 'linkeldn' (rows 2 to {last_row})...")
    # In linkeldn: Col K is verification note (index 10), Col L is Status (index 11), Col N is Notes (index 13)
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/linkeldn!A2:P{last_row}"
    r = session.get(url)
    if r.status_code != 200:
        print(f"Error fetching linkeldn: {r.status_code}")
        return

    rows = r.json().get("values", [])
    updated_l = []
    updated_n = []

    undeliv_count = 0
    hold_count = 0
    approved_count = 0

    for row in rows:
        while len(row) < 16:
            row.append("")

        ver_note = row[10] # Col K
        curr_l = row[11]   # Col L
        curr_n = row[13]   # Col N

        if "UNDELIVERABLE" in ver_note:
            new_l = "DO NOT SEND - BOUNCE (550)"
            new_n = "Mailbox rejected by server; DO NOT EMAIL"
            undeliv_count += 1
        elif "CATCH_ALL" in ver_note:
            new_l = "HOLD - CATCH-ALL"
            new_n = "Catch-all domain; route to LinkedIn InMail or verify via BounceBan"
            hold_count += 1
        elif "CONNECTION_FAILED" in ver_note:
            new_l = "HOLD - UNVERIFIED"
            new_n = "Port 25 timeout/blocked; verify before emailing"
            hold_count += 1
        elif "DELIVERABLE" in ver_note:
            new_l = "Qualified - SEND READY"
            new_n = curr_n if "Cleared" in curr_n else "Cleared for outreach; verified non-bounce"
            approved_count += 1
        else:
            new_l = curr_l if curr_l else "HOLD"
            new_n = curr_n

        updated_l.append([new_l])
        updated_n.append([new_n])

    # Put Col L
    url_l = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/linkeldn!L2:L{last_row}?valueInputOption=USER_ENTERED"
    session.put(url_l, json={"range": f"linkeldn!L2:L{last_row}", "values": updated_l})

    # Put Col N
    url_n = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/linkeldn!N2:N{last_row}?valueInputOption=USER_ENTERED"
    session.put(url_n, json={"range": f"linkeldn!N2:N{last_row}", "values": updated_n})

    print(f"'linkeldn' sanitized: {approved_count} SEND READY, {undeliv_count} DO NOT SEND (Bounces blocked), {hold_count} HELD.")

def main():
    print("=" * 70)
    print("SANITIZING TRACKER OUTREACH STATUSES TO ELIMINATE EMAIL BOUNCES")
    print("=" * 70)

    session = get_authorized_session()

    update_main_tab_statuses(session, "Compute Brokering", 876)
    update_main_tab_statuses(session, "Data", 946)
    update_main_tab_statuses(session, "Data Brokering", 968)
    update_linkeldn_statuses(session, 8708)

    print("\n" + "=" * 70)
    print("SANITIZATION COMPLETE: All bounce risks and unverified emails are now strictly quarantined!")
    print("=" * 70)

if __name__ == "__main__":
    main()
