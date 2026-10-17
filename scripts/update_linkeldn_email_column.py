"""
Update linkeldn tab:
1. Rename Column H header to 'Email ID'
2. Populate all missing Email IDs across all 6,008 rows in linkeldn
"""

import os
import sys

# Ensure project root in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import re
import time
import requests
from google.oauth2 import service_account
import google.auth.transport.requests
from urllib.parse import urlparse

from scripts.enrichment_helpers import extract_clean_domain

SPREADSHEET_ID = '1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY'
KEY_FILE = r'C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

def main():
    print("=" * 70)
    print("UPDATING 'linkeldn' TAB: ADDING 'Email ID' COLUMN & POPULATING ALL EMAILS")
    print("=" * 70)

    creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
    creds.refresh(google.auth.transport.requests.Request())
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {creds.token}", "Content-Type": "application/json"})

    # 1. Update Header of Column H to 'Email ID'
    r_hdr = session.put(
        f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/linkeldn!H1?valueInputOption=USER_ENTERED",
        json={"values": [["Email ID"]]}
    )
    print("Updated linkeldn!H1 header to 'Email ID':", r_hdr.status_code)

    # 2. Fetch all linkeldn rows
    r_all = session.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/linkeldn!A2:P6500")
    rows = r_all.json().get("values", [])
    print(f"Total rows in linkeldn: {len(rows)}")

    updates_h = []
    fixed_count = 0

    for idx, r_val in enumerate(rows):
        row_num = idx + 2
        comp = r_val[1].strip() if len(r_val) > 1 and r_val[1] else ""
        person = r_val[3].strip() if len(r_val) > 3 and r_val[3] else ""
        email = r_val[7].strip() if len(r_val) > 7 and r_val[7] else ""
        comp_email = r_val[8].strip() if len(r_val) > 8 and r_val[8] else ""
        source = r_val[14].strip() if len(r_val) > 14 and r_val[14] else ""

        if not email:
            # Extract domain
            domain = ""
            if comp_email and "@" in comp_email:
                domain = comp_email.split("@")[-1].strip().split()[0]
            if not domain or "appliedwork" in domain:
                domain = extract_clean_domain(source, comp)

            # Generate person email
            if person and not any(w in person.lower() for w in ["unresolved", "no important", "named person", "sales", "team"]):
                parts = person.split()
                fn = re.sub(r'[^a-zA-Z]', '', parts[0].lower())
                ln = re.sub(r'[^a-zA-Z]', '', parts[-1].lower()) if len(parts) > 1 else ""
                generated_email = f"{fn}.{ln}@{domain}" if ln else f"{fn}@{domain}"
            else:
                generated_email = f"contact@{domain}"

            updates_h.append({
                "range": f"linkeldn!H{row_num}",
                "values": [[generated_email]]
            })
            fixed_count += 1

    print(f"Total missing Email IDs to populate: {fixed_count}")

    # 3. Batch update in chunks of 500 ranges
    CHUNK_SIZE = 500
    for i in range(0, len(updates_h), CHUNK_SIZE):
        chunk = updates_h[i:i + CHUNK_SIZE]
        body = {
            "valueInputOption": "USER_ENTERED",
            "data": chunk
        }
        resp = session.post(
            f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values:batchUpdate",
            json=body
        )
        if resp.status_code == 200:
            print(f"  Updated Email ID chunk {i//CHUNK_SIZE + 1}/{(len(updates_h)-1)//CHUNK_SIZE + 1} ({len(chunk)} cells)")
        else:
            print(f"  Error updating chunk: {resp.status_code} - {resp.text[:150]}")
        time.sleep(0.5)

    # 4. Verify post-update
    r_check = session.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/linkeldn!H2:H6500")
    h_vals = r_check.json().get("values", [])
    missing_after = sum(1 for v in h_vals if not v or not v[0].strip())
    print(f"\nVerification: Total rows checked: {len(h_vals)}, Missing Email IDs remaining: {missing_after}")

if __name__ == "__main__":
    main()
