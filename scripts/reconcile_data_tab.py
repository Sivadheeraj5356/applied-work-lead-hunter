import csv
import json
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

# 1. Get sheet metadata
r_meta = session.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?fields=sheets.properties")
sheets = r_meta.json().get("sheets", [])
sheet_map = {s["properties"]["title"]: s["properties"]["sheetId"] for s in sheets}
data_sheet_id = sheet_map["Data"]
print(f"Data sheetId: {data_sheet_id}")

# 2. Inspect rows 461 to 463 and 511 to 513 before deletion
r_check = session.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/Data!A460:D515")
vals = r_check.json().get("values", [])
print(f"Read {len(vals)} rows around 460-515")

# 3. Delete rows 462 to 511 (50 rows: 0-indexed startIndex=461, endIndex=511)
# Note: Google Sheets API deleteDimension is 0-indexed, endIndex is exclusive.
# Row 462 is index 461. Row 511 is index 510.
# So startIndex=461, endIndex=511 will delete rows 462 through 511 (50 rows).
delete_body = {
    "requests": [
        {
            "deleteDimension": {
                "range": {
                    "sheetId": data_sheet_id,
                    "dimension": "ROWS",
                    "startIndex": 461,
                    "endIndex": 511
                }
            }
        }
    ]
}
r_del = session.post(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}:batchUpdate", json=delete_body)
print("Delete rows 462-511 response:", r_del.status_code, r_del.text[:200])

# 4. Check what is now at row 461 and 462
r_after = session.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/Data!A460:D465")
print("After deletion rows 460-465:")
for row in r_after.json().get("values", []):
    print(" ", row)

# 5. Check what is now at row 545 to 547
r_546 = session.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/Data!A545:D550")
print("Rows 545-550:")
for row in r_546.json().get("values", []):
    print(" ", row)

# 6. Clear any residual data in Data!A547:ZZ750
r_clear = session.post(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/Data!A547:ZZ750:clear")
print("Cleared residual Data!A547:ZZ750:", r_clear.status_code)

# 7. Read the 100 Data leads from batch_300_20261017/Data_100.csv
with open(r"C:\Users\E-siva-dheeraj\applied-work\exports\batch_300_20261017\Data_100.csv", "r", encoding="utf-8") as f:
    data_100_rows = list(csv.reader(f))

print(f"Loaded {len(data_100_rows)} Data rows to write starting at A547:Z{547 + len(data_100_rows) - 1}")

# 8. Write the 100 rows into Data!A547:Z646
put_body = {
    "range": f"Data!A547:Z{547 + len(data_100_rows) - 1}",
    "values": data_100_rows
}
r_put = session.put(
    f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/Data!A547:Z{547 + len(data_100_rows) - 1}?valueInputOption=USER_ENTERED",
    json=put_body
)
print("PUT 100 Data rows status:", r_put.status_code)
if r_put.status_code == 200:
    print("Updated range:", r_put.json().get("updatedRange"))
else:
    print("Error:", r_put.text)

# 9. Verify live Data Summary
r_sum = session.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/'Data Summary'!A1:G15")
print("\n=== LIVE DATA SUMMARY ===")
for r in r_sum.json().get("values", []):
    clean = [c for c in r if str(c).strip()]
    if clean:
        print(" | ".join(clean))
