import csv

with open(r'C:\Users\E-siva-dheeraj\applied-work\exports\batch_50_data_20261016\linkeldn_50_data_contacts_gid_910004.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    deliverables = [r for r in reader if 'STATUS=DELIVERABLE' in r['Email verification']]

print(f"Total Deliverable Persons: {len(deliverables)}")
for d in deliverables:
    print(f"{d['Company']} | {d['Person']} ({d['Role / historical affiliation']}) -> {d['Person/selected email candidate']}")
