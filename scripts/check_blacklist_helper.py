import re

with open(r'C:\Users\E-siva-dheeraj\applied-work\tracker_data\live_blacklist_set.txt', 'r', encoding='utf-8') as f:
    blacklist = [line.strip().lower() for line in f if line.strip()]

def normalize(name):
    n = name.lower().strip()
    n = re.sub(r'\b(inc|llc|corp|ltd|limited|co|ai|io|technologies|solutions|group|labs)\b', '', n)
    return re.sub(r'[^a-z0-9]', '', n)

norm_set = set(normalize(b) for b in blacklist)

def check_candidates(candidates):
    clean = []
    dups = []
    for c in candidates:
        if normalize(c) in norm_set:
            dups.append(c)
        else:
            clean.append(c)
    print(f"Checked {len(candidates)} candidates: {len(clean)} novel, {len(dups)} duplicates.")
    if dups:
        print("Duplicates found:", dups[:10])
    return clean

print(f"Blacklist loaded: {len(norm_set)} normalized items.")
