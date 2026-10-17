import requests
from google.oauth2 import service_account
import google.auth.transport.requests

SPREADSHEET_ID = "1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY"
KEY_FILE = r"C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

session = requests.Session()
session.headers.update({"Authorization": f"Bearer {creds.token}"})

tabs = ["Compute Brokering", "Data", "Data Brokering", "Daily Signals", "linkeldn", "Daily Research Log"]

for t in tabs:
    # Look at rows 1 to 10
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/'{t}'!A1:Z10"
    r = session.get(url)
    if r.status_code == 200:
        vals = r.json().get("values", [])
        print(f"=== {t} ===")
        print(f"Total sample rows returned: {len(vals)}")
        for i, row in enumerate(vals[:9]):
            if any(row):
                print(f" Row {i+1}:", row[:6])
    else:
        print(f"Error fetching {t}: {r.status_code} - {r.text}")
