import csv
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
session.headers.update({
    "Authorization": f"Bearer {creds.token}",
    "Content-Type": "application/json"
})

# 1. Clear Data!N462:ZZ560
clear_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/Data!N462:ZZ560:clear"
r_clear = session.post(clear_url)
print("Cleared shifted range:", r_clear.status_code)

# 2. Prepare the 85 Data rows
def read_csv_rows(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return list(csv.reader(f))

data_b1 = read_csv_rows(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_150_20261016\Data_50_gid_156275556.csv")
data_b2 = read_csv_rows(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_50_data_20261016\Data_main_tab_gid_156275556.csv")
all_data_rows = data_b1 + data_b2

print(f"Total rows to put into Data starting at A462: {len(all_data_rows)}")

# 3. Put directly to Data!A462
put_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/Data!A462:Z{462 + len(all_data_rows) - 1}?valueInputOption=USER_ENTERED"
body = {
    "range": f"Data!A462:Z{462 + len(all_data_rows) - 1}",
    "values": all_data_rows
}
r_put = session.put(put_url, json=body)
print("PUT response status:", r_put.status_code)
if r_put.status_code == 200:
    print("Updated range:", r_put.json().get("updatedRange"))
else:
    print("Error:", r_put.text)

# 4. Verify row 462
verify_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/Data!A462:F464"
r_ver = session.get(verify_url)
print("Verified Data A462:F464:")
for row in r_ver.json().get("values", []):
    print(" ", row)
