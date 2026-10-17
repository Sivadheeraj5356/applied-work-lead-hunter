import requests
from google.oauth2 import service_account
import google.auth.transport.requests

SPREADSHEET_ID = '1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY'
KEY_FILE = r'C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json'
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])
creds.refresh(google.auth.transport.requests.Request())
session = requests.Session()
session.headers.update({'Authorization': f'Bearer {creds.token}', 'Content-Type': 'application/json'})

# 1. Check if sheet already exists
r = session.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?fields=sheets.properties")
sheets = r.json().get('sheets', [])
sheet_titles = [s['properties']['title'] for s in sheets]
print("Existing sheets:", sheet_titles)

new_tab_name = "Company Data Leads"
if new_tab_name not in sheet_titles:
    body = {
        "requests": [
            {
                "addSheet": {
                    "properties": {
                        "title": new_tab_name,
                        "gridProperties": {
                            "rowCount": 3000,
                            "columnCount": 20
                        }
                    }
                }
            }
        ]
    }
    r_add = session.post(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}:batchUpdate", json=body)
    print(f"Created sheet '{new_tab_name}':", r_add.status_code)
else:
    print(f"Sheet '{new_tab_name}' already exists.")
