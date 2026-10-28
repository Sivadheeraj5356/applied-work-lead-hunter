import sys
sys.path.insert(0, r"C:\Users\E-siva-dheeraj\applied-work")
from src.core.verifier import verify_single_email

candidates = [
    ("Amplify Partners", "Sarah Catanzaro", "sarah.catanzaro@amplifypartners.com", "Modal, Runway, Prefect"),
    ("Amplify Partners", "Sunil Dhaliwal", "sunil@amplifypartners.com", "Modal, Datadog, dbt Labs"),
    ("Chemistry VC", "Ethan Kurzweil", "ethan@chemistry.vc", "Twitch, LaunchDarkly, PagerDuty"),
    ("Root Ventures", "Lee Edwards", "lee@root.vc", "Great Expectations, Esper"),
    ("Root Ventures", "Kane Hsieh", "kane@root.vc", "Instrumental, Dusty Robotics"),
    ("Decibel Partners", "Alessio Fanelli", "alessio@decibel.vc", "Modal, Fireworks.ai, E2B"),
    ("Zetta Venture Partners", "Jocelyn Goldfein", "jocelyn@zettavp.com", "Domino Data Lab, Tractable"),
    ("Costanoa Ventures", "Greg Sands", "greg@costanoavc.com", "Alation, Fivetran"),
    ("Costanoa Ventures", "John Cowgill", "john@costanoavc.com", "Keen IO, Astronomer, Hightouch"),
    ("Afore Capital", "Gaurav Jain", "gaurav@afore.vc", "Afore pre-seed AI portfolio"),
    ("Susa Ventures", "Chad Byers", "chad@susaventures.com", "Scale AI, Flexport, Robinhood"),
    ("Bloomberg Beta", "Roy Bahat", "roy@bloombergbeta.com", "DeepSee, Zapier, Primer AI"),
    ("Bloomberg Beta", "James Cham", "james@bloombergbeta.com", "Domino Data Lab, Context.io"),
    ("Eniac Ventures", "Nihal Mehta", "nihal@eniac.vc", "Bedrock, Ironclad, Alloy"),
    ("Homebrew", "Satya Patel", "satya@homebrew.co", "Finix, Plaid, Gusto"),
    ("SV Angel", "Topher Conway", "topher@svangel.com", "Scale AI, Stripe, Airbnb"),
    ("Lux Capital", "Brandon Reeves", "brandon.reeves@luxcapital.com", "Applied Intuition, Runway, Hugging Face")
]

print("Running real-time SMTP verification on candidate queue...")
verified_candidates = []
for firm, name, email, ref in candidates:
    res = verify_single_email(email)
    st = res.get("status")
    det = res.get("details")
    print(f"{name} ({email}) -> status: {st}, details: {det}")
    if st == "DELIVERABLE":
        verified_candidates.append((firm, name, email, ref))

print(f"\nTotal verified non-catchall deliverable candidates: {len(verified_candidates)}")
for c in verified_candidates:
    print(f"  READY: {c[1]} <{c[2]}> ({c[0]})")
