import requests
from google.oauth2 import service_account
import google.auth.transport.requests

SPREADSHEET_ID = '1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY'
KEY_FILE = r'C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json'
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])
creds.refresh(google.auth.transport.requests.Request())
session = requests.Session()
session.headers.update({'Authorization': f'Bearer {creds.token}'})

# 1. Verify linkeldn headers and sample
r_li = session.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/linkeldn!A1:I5")
print("=== 'linkeldn' Tab Headers & Sample ===")
for i, r in enumerate(r_li.json().get('values', [])):
    col_h = r[7] if len(r) > 7 else ""
    col_b = r[1] if len(r) > 1 else ""
    col_d = r[3] if len(r) > 3 else ""
    print(f"Row {i+1}: Col H='{col_h}' | Col B='{col_b}' | Col D='{col_d}'")

# 2. Verify Company Data Leads headers and sample
r_cd = session.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/'Company Data Leads'!A1:K6")
print("\n=== 'Company Data Leads' Tab Headers & Sample ===")
for i, r in enumerate(r_cd.json().get('values', [])):
    print(f"Row {i+1}:")
    print(f"  Company: {r[0] if len(r)>0 else ''}")
    print(f"  Category: {r[1] if len(r)>1 else ''}")
    print(f"  Person: {r[2] if len(r)>2 else ''}")
    print(f"  Title: {r[3] if len(r)>3 else ''}")
    print(f"  Email ID: {r[4] if len(r)>4 else ''}")
    print(f"  Info & Data: {r[8][:100] if len(r)>8 else ''}...")
    print(f"  Signal: {r[9] if len(r)>9 else ''}")

# 3. Check live summaries
for sum_tab in ["Compute Brokering Summary", "Data Summary", "Data Brokering Summary"]:
    r_sum = session.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/'{sum_tab}'!A6:C8")
    vals = r_sum.json().get("values", [])
    print(f"\n{sum_tab}: {vals[0] if vals else 'EMPTY'}")
