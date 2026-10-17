import json

with open(r'C:\Users\E-siva-dheeraj\applied-work\tracker_data\enrichment_targets.json', 'r', encoding='utf-8') as f:
    targets = json.load(f)

missing_contact = [t for t in targets if t['is_missing_contact']]
print(f"Total missing contact leads: {len(missing_contact)}")

by_tab = {}
for t in missing_contact:
    by_tab.setdefault(t['tab'], []).append(t)

for tab, lst in by_tab.items():
    print(f"\n=== {tab} ({len(lst)} missing contacts) ===")
    for t in lst[:10]:
        print(f"Row {t['row_num']}: {t['company']} | Existing Contact: '{t['contact']}' | Existing Email: '{t['email']}' | Web: {t['website'].splitlines()[0] if t['website'] else 'None'}")
