import requests
from google.oauth2 import service_account
import google.auth.transport.requests

SPREADSHEET_ID = '1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY'
KEY_FILE = r'C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json'
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])
creds.refresh(google.auth.transport.requests.Request())
s = requests.Session()
s.headers.update({'Authorization': f'Bearer {creds.token}'})

r = s.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/linkeldn!A2:H6500")
rows = r.json().get('values', [])
print(f"Total rows in linkeldn: {len(rows)}")

empty_email_count = 0
for idx, r_val in enumerate(rows):
    email = r_val[7].strip() if len(r_val) > 7 and r_val[7] else ''
    if not email:
        empty_email_count += 1

print(f"Rows with empty Column H in linkeldn: {empty_email_count}")
