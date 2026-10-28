import requests
from google.oauth2 import service_account
import google.auth.transport.requests

KEY_FILE = r"C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json"
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=["https://www.googleapis.com/auth/spreadsheets"])
creds.refresh(google.auth.transport.requests.Request())
headers = {"Authorization": f"Bearer {creds.token}"}

for tab in ["Data", "Data Brokering", "Compute Brokering"]:
    url = f"https://sheets.googleapis.com/v4/spreadsheets/1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY/values/'{tab}'!A1:B1300"
    res = requests.get(url, headers=headers).json()
    vals = res.get("values", [])
    non_empty = 0
    for idx, r in enumerate(vals, 1):
        if r and any(str(x).strip() for x in r):
            non_empty = idx
    print(f"{tab}: total returned {len(vals)}, last non-empty row index: {non_empty}")
