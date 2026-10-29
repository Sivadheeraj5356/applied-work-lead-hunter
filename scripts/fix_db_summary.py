import requests
from google.oauth2 import service_account
import google.auth.transport.requests

KEY_FILE = r"C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json"
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=["https://www.googleapis.com/auth/spreadsheets"])
creds.refresh(google.auth.transport.requests.Request())
headers = {"Authorization": f"Bearer {creds.token}"}

url = "https://sheets.googleapis.com/v4/spreadsheets/1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY/values/'Data Brokering Summary'!C6:C7?valueInputOption=USER_ENTERED"
body = {
    "range": "'Data Brokering Summary'!C6:C7",
    "values": [
        ["=COUNTIF('Data Brokering'!A9:A1500,\"<>\")"],
        ["=IFERROR(COUNTUNIQUE(FILTER('Data Brokering'!A9:A1500,'Data Brokering'!A9:A1500<>\"\")),0)"]
    ]
}
r = requests.put(url, headers=headers, json=body)
print("Updated summary formula status:", r.status_code)

url2 = "https://sheets.googleapis.com/v4/spreadsheets/1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY/values/'Data Brokering Summary'!A5:D8"
res2 = requests.get(url2, headers=headers).json()
for row in res2.get("values", []):
    print(row)
