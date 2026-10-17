import requests
from google.oauth2 import service_account
import google.auth.transport.requests

SPREADSHEET_ID = '1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY'
KEY_FILE = r'C:\Users\E-siva-dheeraj\applied-work\config\google_service_account.json'
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])
creds.refresh(google.auth.transport.requests.Request())
s = requests.Session()
s.headers.update({'Authorization': f'Bearer {creds.token}'})

for tab in ['Compute Brokering', 'Data', 'Data Brokering']:
    r = s.get(f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/'{tab}'!A9:T150")
    rows = r.json().get('values', [])
    print(f'=== Sample Missing in {tab} ===')
    count = 0
    for idx, r_val in enumerate(rows):
        comp = r_val[0] if len(r_val)>0 else ''
        contact = r_val[1] if len(r_val)>1 else ''
        role = r_val[2] if len(r_val)>2 else ''
        email = r_val[3] if len(r_val)>3 else ''
        website = r_val[4] if len(r_val)>4 else ''
        person_email = r_val[19] if len(r_val)>19 else ''
        
        is_missing = not contact or not email or 'unresolved' in contact.lower() or 'no important' in contact.lower() or contact.lower() == 'sales'
        if comp and is_missing:
            print(f'Row {idx+9}: Comp="{comp}", Contact="{contact}", Role="{role}", Email="{email}", PersonEmail="{person_email}", Web="{website[:30]}"')
            count += 1
            if count >= 6:
                break
