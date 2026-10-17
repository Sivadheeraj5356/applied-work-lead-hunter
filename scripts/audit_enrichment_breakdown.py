import json
from collections import defaultdict

with open(r'C:\Users\E-siva-dheeraj\applied-work\tracker_data\enrichment_targets.json', 'r', encoding='utf-8') as f:
    targets = json.load(f)

print(f"Total targets: {len(targets)}")

tab_counts = defaultdict(int)
missing_contact_counts = defaultdict(int)
missing_email_counts = defaultdict(int)
li_under_2 = defaultdict(int)
li_under_3 = defaultdict(int)

for t in targets:
    tab = t['tab']
    tab_counts[tab] += 1
    if t['is_missing_contact']:
        missing_contact_counts[tab] += 1
    if t['is_missing_email']:
        missing_email_counts[tab] += 1
    if t['li_count'] < 2:
        li_under_2[tab] += 1
    if t['li_count'] < 3:
        li_under_3[tab] += 1

print("\n--- Summary per tab ---")
for tab in ['Compute Brokering', 'Data', 'Data Brokering']:
    print(f"{tab}:")
    print(f"  Total leads: {tab_counts[tab]}")
    print(f"  Missing contact: {missing_contact_counts[tab]}")
    print(f"  Missing email: {missing_email_counts[tab]}")
    print(f"  Fewer than 2 in linkeldn: {li_under_2[tab]}")
    print(f"  Fewer than 3 in linkeldn: {li_under_3[tab]}")
