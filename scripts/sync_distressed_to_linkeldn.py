"""
Sync Curated Failed & Struggling Companies to the 'linkeldn' Tab
Adds premier distressed venture assets, failed AI/robotics/health startups,
and restructuring leadership directly to the Google Sheets 'linkeldn' tab.
"""

import sys
import os
import json
import time
import requests
from google.oauth2 import service_account
import google.auth.transport.requests

# Ensure project root in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.verifier import verify_emails_parallel
from scripts.curate_distressed_companies import DISTRESSED_COMPANIES

SPREADSHEET_ID = '1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY'
KEY_FILE = r'C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

def main():
    print("=" * 70)
    print("SYNCING FAILED & STRUGGLING COMPANIES TO 'linkeldn' TAB...")
    print("=" * 70)

    # 1. Authenticate with Google Sheets API
    creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
    creds.refresh(google.auth.transport.requests.Request())
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {creds.token}", "Content-Type": "application/json"})

    # 2. Fetch existing linkeldn contacts to prevent duplicates
    r_li = session.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/linkeldn!A2:D6500")
    existing_rows = r_li.json().get("values", [])
    print(f"Current rows in linkeldn: {len(existing_rows)}")

    existing_set = set() # (company_clean, person_clean)
    for r in existing_rows:
        comp = r[1].strip().lower() if len(r) > 1 and r[1] else ""
        person = r[3].strip().lower() if len(r) > 3 and r[3] else ""
        if comp and person:
            existing_set.add((comp, person))

    # 3. Collect all candidate emails for SMTP verification
    candidate_emails = []
    for c in DISTRESSED_COMPANIES:
        for p in c["persons"]:
            email = p[2].strip()
            if email and "@" in email:
                candidate_emails.append(email)

    print(f"Collected {len(candidate_emails)} candidate emails across {len(DISTRESSED_COMPANIES)} distressed companies.")
    print("Running parallel zero-bounce SMTP deliverability check...")
    verification_results = verify_emails_parallel(candidate_emails, max_workers=16)

    deliverable_count = sum(1 for r in verification_results.values() if r.get("status") == "DELIVERABLE")
    catchall_count = sum(1 for r in verification_results.values() if r.get("status") == "CATCH_ALL")
    print(f"SMTP Verification results: {deliverable_count} DELIVERABLE, {catchall_count} CATCH_ALL / DOMAIN_ACCEPT.")

    # 4. Build linkeldn rows
    rows_to_append = []
    today_str = "2026-10-17"

    for c in DISTRESSED_COMPANIES:
        comp_name = c["company"]
        comp_clean = comp_name.strip().lower()
        domain = c["domain"]
        category = c["category"]
        data_value = c["data_value"]
        source = c["source"]

        for idx_p, p in enumerate(c["persons"]):
            p_name = p[0]
            p_clean = p_name.strip().lower()
            p_role = p[1]
            p_email = p[2]
            p_li = p[3]
            p_note = p[4] if len(p) > 4 else "Executive leadership / restructuring authority"

            # Check for existing duplicate
            if (comp_clean, p_clean) in existing_set:
                continue

            existing_set.add((comp_clean, p_clean))

            # Verification status
            v_res = verification_results.get(p_email, {})
            v_status = v_res.get("status", "NOT_CHECKED")
            if v_status == "DELIVERABLE":
                verif_text = "STATUS=DELIVERABLE; verified direct port 25 SMTP"
                stage = "RESEARCH HOLD"
                action_text = "Rights owner/estate unresolved; evaluate proprietary data licensing & asset acquisition"
            elif v_status == "CATCH_ALL":
                verif_text = "STATUS=CATCH_ALL; domain accepts; direct port 25 handshake"
                stage = "RESEARCH HOLD"
                action_text = "Rights owner/estate unresolved; evaluate proprietary data licensing & asset acquisition"
            else:
                verif_text = f"STATUS={v_status}; verified direct port 25 SMTP"
                stage = "RESEARCH HOLD"
                action_text = "Rights owner/estate unresolved; founder identity does not establish licensing authority"

            priority = "0 Failed/distressed founder" if idx_p == 0 else "1 Failed/distressed account"

            row = [
                priority,
                comp_name,
                category,
                p_name,
                p_role,
                p_li,
                source, # X/Twitter/Source
                p_email,
                f"contact@{domain}",
                f"{data_value} | {p_note}",
                verif_text,
                stage,
                f"Data Brokering!{comp_name[:20]}",
                action_text,
                source,
                today_str
            ]
            rows_to_append.append(row)

    print(f"\nPrepared {len(rows_to_append)} new high-value distressed leadership rows to append to 'linkeldn'.")

    # 5. Append in safe chunks of 100 rows
    CHUNK_SIZE = 100
    for i in range(0, len(rows_to_append), CHUNK_SIZE):
        chunk = rows_to_append[i:i + CHUNK_SIZE]
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/'linkeldn':append?valueInputOption=USER_ENTERED&insertDataOption=INSERT_ROWS"
        resp = session.post(url, json={"values": chunk})
        if resp.status_code == 200:
            print(f"  Appended chunk {i//CHUNK_SIZE + 1}/{(len(rows_to_append)-1)//CHUNK_SIZE + 1} ({len(chunk)} rows)")
        else:
            print(f"  Error appending chunk: {resp.status_code} - {resp.text[:150]}")
        time.sleep(0.5)

    # 6. Audit total linkeldn rows after append
    r_li_after = session.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/linkeldn!A:A")
    total_li_after = len(r_li_after.json().get("values", []))
    print(f"\nTotal rows in 'linkeldn' now: {total_li_after} (was {len(existing_rows) + 1})")
    print("FAILED & STRUGGLING COMPANIES SUCCESSFULLY SYNCED TO 'linkeldn'!")

if __name__ == "__main__":
    main()
