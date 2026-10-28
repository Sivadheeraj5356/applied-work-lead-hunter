import sys
sys.path.insert(0, r"C:\Users\E-siva-dheeraj\applied-work")
from src.core.verifier import verify_single_email

queue_2 = [
    ("Amplify Partners", "Sunil Dhaliwal", "sunil@amplifypartners.com", "Modal and dbt Labs"),
    ("Root Ventures", "Kane Hsieh", "kane@root.vc", "Instrumental and Dusty Robotics"),
    ("Susa Ventures", "Leo Polovets", "leo@susaventures.com", "Scale AI and Fastly"),
    ("Eniac Ventures", "Tim Young", "tim@eniac.vc", "enterprise AI and cloud infrastructure"),
    ("Fuel Capital", "Chris Howard", "chris@fuelcapital.com", "Cloudflare and CoreOS"),
    ("Fuel Capital", "Leah Busque Solivan", "leah@fuelcapital.com", "marketplace infrastructure"),
    ("Precursor Ventures", "Charles Hudson", "charles@precursorvc.com", "pre-seed enterprise software"),
    ("Homebrew", "Hunter Walk", "hunter@homebrew.co", "Plaid and Cruise"),
    ("Everywhere Ventures", "Jenny Fielding", "jenny@everywhere.vc", "pre-seed AI and B2B platforms"),
    ("Haystack", "Semil Shah", "semil@haystack.vc", "Figma and HashiCorp"),
    ("BoxGroup", "David Tisch", "david@boxgroup.com", "Plaid and Ramp"),
    ("BoxGroup", "Adam Rothenberg", "adam@boxgroup.com", "enterprise and infrastructure tooling"),
    ("Work-Bench", "Jonathan Lehr", "jonathan@work-bench.com", "Cockroach Labs and Arthur AI"),
    ("Work-Bench", "Jessica Lin", "jessica@work-bench.com", "Courier and Arthur AI"),
    ("LAUNCH / The Syndicate", "Jason Calacanis", "jason@calacanis.com", "Robinhood and early B2B tech"),
    ("Equal Ventures", "Rick Zullo", "rick@equal.vc", "supply chain and data infrastructure"),
    ("Dynamo Ventures", "Santosh Sankar", "santosh@dynamo.vc", "industrial and supply chain data"),
    ("Basis Set Ventures", "Lan Xuezhao", "lan@basisset.com", "AI-first workflows and data infrastructure")
]

print(f"Verifying {len(queue_2)} candidate addresses via local SMTP handshake...")
verified_queue = []
for firm, name, email, ref in queue_2:
    res = verify_single_email(email)
    st = res.get("status")
    det = res.get("details")
    print(f"{name} ({email}) -> {st} ({det})")
    if st == "DELIVERABLE":
        verified_queue.append((firm, name, email, ref))

print(f"\nTotal verified non-catchall DELIVERABLE for Batch 2: {len(verified_queue)}")
for c in verified_queue:
    print(f"  READY: {c[1]} <{c[2]}> | {c[0]} | Hook: {c[3]}")
