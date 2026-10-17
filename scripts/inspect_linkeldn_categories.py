import requests
from google.oauth2 import service_account
import google.auth.transport.requests
from collections import Counter

SPREADSHEET_ID = '1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY'
KEY_FILE = r'C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json'
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])
creds.refresh(google.auth.transport.requests.Request())
s = requests.Session()
s.headers.update({'Authorization': f'Bearer {creds.token}'})

r = s.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/linkeldn!A2:C6500")
rows = r.json().get('values', [])
print(f"Total rows in linkeldn: {len(rows)}")

categories = Counter()
for r in rows:
    cat = r[2].strip() if len(r) > 2 and r[2] else 'Unknown'
    categories[cat] += 1

print("\nBreakdown by Category in linkeldn:")
for cat, count in categories.most_common():
    print(f"  {cat}: {count} rows")
