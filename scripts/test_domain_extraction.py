import json
import re
from urllib.parse import urlparse

with open(r'C:\Users\E-siva-dheeraj\applied-work\tracker_data\enrichment_targets.json', 'r', encoding='utf-8') as f:
    targets = json.load(f)

def extract_domain(website, company):
    if website:
        for line in website.splitlines():
            line = line.strip()
            if 'http' in line:
                try:
                    parsed = urlparse(line)
                    netloc = parsed.netloc.lower()
                    if netloc.startswith('www.'):
                        netloc = netloc[4:]
                    # ignore non-company domains
                    if netloc and not any(d in netloc for d in ['linkedin.com', 'x.com', 'twitter.com', 'huggingface.co', 'github.com', 'google.com', 'youtube.com']):
                        return netloc.split(':')[0]
                except Exception:
                    pass
    # fallback to cleaned company name
    clean_comp = re.sub(r'[^a-zA-Z0-9]', '', company.lower())
    return f"{clean_comp}.com"

domain_map = {}
for t in targets:
    dom = extract_domain(t['website'], t['company'])
    domain_map[t['company']] = dom

print(f"Mapped {len(domain_map)} companies to domains.")
print("Sample domain mappings:")
for c in list(domain_map.keys())[:15]:
    print(f"  '{c}' -> {domain_map[c]}")
