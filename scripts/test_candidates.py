import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.append(r'C:\Users\E-siva-dheeraj\applied-work\scripts')
from verify_email import verify_single_email

test_candidates = [
    # Compute Brokering / AI Infra
    'karol@pi.website',
    'deepak@skild.ai',
    'ali@fieldai.com',
    'karan@cartesia.ai',
    'tuhin@baseten.co',
    # Data
    'freddie@ayadata.ai',
    'ama@ayadata.ai',
    # Data Brokering
    'pranav@drongoai.com',
    'raveesh@drongoai.com',
    'angel@quibim.com',
    'charles.kariuki@premierhospital.org',
    'victoria.njeru@premierhospital.org',
    'jeremy@naluri.life',
    'azran@naluri.life'
]

print(f"Starting parallel verification of {len(test_candidates)} candidates...\n", flush=True)

def check_one(em):
    res = verify_single_email(em)
    return em, res

results = []
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(check_one, em) for em in test_candidates]
    for fut in as_completed(futures):
        em, res = fut.result()
        results.append(res)
        status = res.get('status')
        details = res.get('details')
        print(f"[{status}] {em} -> {details}", flush=True)

print("\n--- Summary of Verified Deliverable (250 OK) ---", flush=True)
deliv = [r for r in results if r.get('status') == 'DELIVERABLE']
for d in deliv:
    print(f"DELIVERABLE: {d['email']} (MX: {d.get('mx')})", flush=True)
