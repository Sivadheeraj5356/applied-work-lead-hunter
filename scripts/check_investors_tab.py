import requests
from google.oauth2 import service_account
import google.auth.transport.requests

KEY_FILE = r"C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json"
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=["https://www.googleapis.com/auth/spreadsheets"])
creds.refresh(google.auth.transport.requests.Request())
headers = {"Authorization": f"Bearer {creds.token}"}
url = "https://sheets.googleapis.com/v4/spreadsheets/1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY/values/Investors!A1:Z20"
res = requests.get(url, headers=headers).json()
print("Values in Investors:", res.get("values", []))
