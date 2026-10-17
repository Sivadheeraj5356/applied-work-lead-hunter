"""
Google Sheets REST API Client
Provides authenticated append and batch-write capabilities using Google Service Account credentials.
"""

import requests
from google.oauth2 import service_account
import google.auth.transport.requests

class SheetsClient:
    def __init__(self, key_file=r"C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json", 
                 spreadsheet_id="1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY"):
        self.key_file = key_file
        self.spreadsheet_id = spreadsheet_id
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        self.session = self._init_session()

    def _init_session(self):
        creds = service_account.Credentials.from_service_account_file(self.key_file, scopes=self.scopes)
        auth_req = google.auth.transport.requests.Request()
        creds.refresh(auth_req)
        s = requests.Session()
        s.headers.update({
            "Authorization": f"Bearer {creds.token}",
            "Content-Type": "application/json"
        })
        return s

    def get_sheet_metadata(self):
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{self.spreadsheet_id}?fields=sheets.properties"
        resp = self.session.get(url)
        if resp.status_code == 200:
            return resp.json().get("sheets", [])
        return []

    def append_rows(self, tab_name, rows, chunk_size=50):
        """Appends rows in chunks to prevent payload timeouts."""
        if not rows:
            return True
            
        success = True
        for i in range(0, len(rows), chunk_size):
            chunk = rows[i:i + chunk_size]
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{self.spreadsheet_id}/values/'{tab_name}':append?valueInputOption=USER_ENTERED&insertDataOption=INSERT_ROWS"
            body = {"values": chunk}
            resp = self.session.post(url, json=body)
            if resp.status_code == 200:
                print(f"Appended chunk {i//chunk_size + 1}/{(len(rows)-1)//chunk_size + 1} to '{tab_name}' ({len(chunk)} rows)")
            else:
                print(f"Error appending to '{tab_name}': {resp.status_code} - {resp.text}")
                success = False
        return success
