import json
from urllib.parse import urlparse
import re

with open(r'C:\Users\E-siva-dheeraj\applied-work\tracker_data\enrichment_targets.json', 'r', encoding='utf-8') as f:
    targets = json.load(f)

missing_contact = [t for t in targets if t['is_missing_contact']]
print(f"Total missing contact leads: {len(missing_contact)}")

with open(r'C:\Users\E-siva-dheeraj\applied-work\tracker_data\missing_contacts_list.json', 'w', encoding='utf-8') as f:
    json.dump([{
        'tab': t['tab'],
        'row_num': t['row_num'],
        'company': t['company'],
        'existing_contact': t['contact'],
        'existing_role': t['role'],
        'existing_email': t['email'],
        'website': t['website'],
        'side': t['side'],
        'requirement': t['requirement']
    } for t in missing_contact], f, indent=2)

print("Saved tracker_data/missing_contacts_list.json")
