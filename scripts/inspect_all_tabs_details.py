import requests
from google.oauth2 import service_account
import google.auth.transport.requests

SPREADSHEET_ID = '1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY'
KEY_FILE = r'C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json'
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])
creds.refresh(google.auth.transport.requests.Request())
s = requests.Session()
s.headers.update({'Authorization': f'Bearer {creds.token}'})

r = s.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?fields=sheets.properties")
sheets = r.json().get('sheets', [])
print("Sheets in spreadsheet:")
for sh in sheets:
    p = sh['properties']
    print(f"  Title: '{p['title']}', sheetId: {p['sheetId']}, index: {p.get('index')}")

# Check linkeldn header row 1
r_li = s.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/linkeldn!A1:Z1")
print("\nlinkeldn Row 1 Headers:")
print(r_li.json().get('values', []))
