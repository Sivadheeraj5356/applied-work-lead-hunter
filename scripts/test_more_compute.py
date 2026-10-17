import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.append(r'C:\Users\E-siva-dheeraj\applied-work\scripts')
from verify_email import verify_single_email

more_candidates = [
    'vipul@together.xyz', 'vipul@together.ai',
    'lin@fireworks.ai',
    'chris@modular.com', 'clattner@modular.com',
    'demi@pika.art',
    'michael@phind.com',
    'dean@decart.ai'
]

print(f"Testing {len(more_candidates)} additional AI compute candidates...\n", flush=True)
with ThreadPoolExecutor(max_workers=8) as ex:
    futs = {ex.submit(verify_single_email, em): em for em in more_candidates}
    for f in as_completed(futs):
        res = f.result()
        st = res.get('status')
        em = res.get('email')
        det = res.get('details')
        print(f"[{st}] {em} -> {det}", flush=True)
