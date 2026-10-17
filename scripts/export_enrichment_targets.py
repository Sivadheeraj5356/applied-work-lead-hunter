import requests
import json
import csv
from google.oauth2 import service_account
import google.auth.transport.requests

SPREADSHEET_ID = '1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY'
KEY_FILE = r'C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json'
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])
creds.refresh(google.auth.transport.requests.Request())
s = requests.Session()
s.headers.update({'Authorization': f'Bearer {creds.token}'})

# 1. Fetch all existing linkeldn rows
r_li = s.get(f'https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/linkeldn!A2:P2500')
li_rows = r_li.json().get('values', [])
li_by_comp = {}
for r in li_rows:
    comp = r[1].strip() if len(r) > 1 and r[1] else ''
    person = r[3].strip() if len(r) > 3 and r[3] else ''
    email = r[7].strip() if len(r) > 7 and r[7] else ''
    role = r[4].strip() if len(r) > 4 and r[4] else ''
    if comp:
        li_by_comp.setdefault(comp.lower(), []).append({'person': person, 'email': email, 'role': role})

print(f"Total linkeldn rows: {len(li_rows)}, unique companies: {len(li_by_comp)}")

# 2. Extract targets from Compute Brokering, Data, Data Brokering
targets = []

for tab in ['Compute Brokering', 'Data', 'Data Brokering']:
    r = s.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/'{tab}'!A9:Y1000")
    rows = r.json().get('values', [])
    for idx, r_val in enumerate(rows):
        row_num = idx + 9
        comp = r_val[0].strip() if len(r_val) > 0 and r_val[0] else ''
        if not comp:
            continue
        contact = r_val[1].strip() if len(r_val) > 1 and r_val[1] else ''
        role = r_val[2].strip() if len(r_val) > 2 and r_val[2] else ''
        email = r_val[3].strip() if len(r_val) > 3 and r_val[3] else ''
        website = r_val[4].strip() if len(r_val) > 4 and r_val[4] else ''
        side = r_val[5].strip() if len(r_val) > 5 and r_val[5] else ''
        req = r_val[6].strip() if len(r_val) > 6 and r_val[6] else ''
        company_email = r_val[18].strip() if len(r_val) > 18 and r_val[18] else ''
        person_email = r_val[19].strip() if len(r_val) > 19 and r_val[19] else ''
        
        is_missing_contact = not contact or any(w in contact.lower() for w in ['unresolved', 'no important', 'named owner', 'named person', 'sales', 'team'])
        is_missing_email = not email or not person_email
        li_contacts = li_by_comp.get(comp.lower(), [])
        
        targets.append({
            'tab': tab,
            'row_num': row_num,
            'company': comp,
            'contact': contact,
            'role': role,
            'email': email,
            'person_email': person_email,
            'company_email': company_email,
            'website': website,
            'side': side,
            'requirement': req,
            'is_missing_contact': is_missing_contact,
            'is_missing_email': is_missing_email,
            'li_count': len(li_contacts),
            'li_contacts': li_contacts
        })

print(f"Total evaluated leads across 3 tabs: {len(targets)}")
missing_contact_leads = [t for t in targets if t['is_missing_contact']]
missing_email_leads = [t for t in targets if t['is_missing_email']]
fewer_than_3_li = [t for t in targets if t['li_count'] < 3]

print(f"Leads with missing/unresolved contact in main tab: {len(missing_contact_leads)}")
print(f"Leads with missing/unresolved email in main tab: {len(missing_email_leads)}")
print(f"Leads with fewer than 3 contacts in linkeldn: {len(fewer_than_3_li)}")

with open(r'C:\Users\E-siva-dheeraj\applied-work\tracker_data\enrichment_targets.json', 'w', encoding='utf-8') as f:
    json.dump(targets, f, indent=2)

print("Saved enrichment targets to tracker_data/enrichment_targets.json")
