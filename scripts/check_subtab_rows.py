import requests
from google.oauth2 import service_account
import google.auth.transport.requests

KEY_FILE = r"C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json"
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=["https://www.googleapis.com/auth/spreadsheets"])
creds.refresh(google.auth.transport.requests.Request())
headers = {"Authorization": f"Bearer {creds.token}"}

subtabs = [
    ("Company Data Leads", "A1:A5000"),
    ("LinkedIn and phone numbers", "A1:A12000"),
    ("Daily Signals", "A1:A3000"),
    ("Daily Research Log", "A1:A100")
]

for tab, rng in subtabs:
    url = f"https://sheets.googleapis.com/v4/spreadsheets/1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY/values/'{tab}'!{rng}"
    res = requests.get(url, headers=headers).json()
    vals = res.get("values", [])
    non_empty = 0
    for idx, r in enumerate(vals, 1):
        if r and any(str(x).strip() for x in r):
            non_empty = idx
    print(f"{tab}: total returned {len(vals)}, last non-empty row index: {non_empty}")
