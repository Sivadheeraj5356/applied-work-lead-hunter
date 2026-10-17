import json
import requests
from google.oauth2 import service_account
import google.auth.transport.requests

SPREADSHEET_ID = "1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY"
KEY_FILE = r"C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json"

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

print("Authenticating with service account...")
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=scopes)
auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)
token = creds.token
print("Authenticated successfully! Token received.")

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?fields=sheets.properties"
resp = requests.get(url, headers=headers)
print("Response status code:", resp.status_code)
if resp.status_code == 200:
    data = resp.json()
    print("SUCCESS! Connected to Google Sheet. Tabs found:")
    for s in data.get("sheets", []):
        props = s.get("properties", {})
        print(f" - {props.get('title')} (id: {props.get('sheetId')})")
else:
    print("Error response:", resp.text)
