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

def read_summary(tab_name):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/'{tab_name}'!A1:G15"
    r = session.get(url)
    if r.status_code == 200:
        vals = r.json().get("values", [])
        print(f"=== LIVE: {tab_name} ===")
        for row in vals:
            clean = [c for c in row if str(c).strip()]
            if clean:
                print(" | ".join(clean))
    else:
        print(f"Error {tab_name}: {r.status_code}")

read_summary("Compute Brokering Summary")
print()
read_summary("Data Summary")
print()
read_summary("Data Brokering Summary")
