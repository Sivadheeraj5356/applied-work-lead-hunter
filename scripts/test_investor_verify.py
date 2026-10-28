import os
import sys

sys.path.insert(0, r"C:\Users\E-siva-dheeraj\applied-work")
from src.core.verifier import verify_emails_parallel

test_emails = [
    "sarah.catanzaro@amplifypartners.com",
    "ed@boldstart.vc",
    "chris@race.capital",
    "alex@2048.vc",
    "d@danielgross.com",
    "nat@nat.org",
    "jason@calacanis.com",
    "aneel@somacap.com",
    "gaurav@afore.vc",
    "topher@svangel.com",
    "boris@versionone.vc",
    "angela@versionone.vc",
    "chip@flybridge.com",
    "jesse@flybridge.com",
    "chad@susaventures.com",
    "leo@susaventures.com",
    "nihal@eniac.vc",
    "satya@homebrew.co",
    "hunter@homebrew.co",
    "pejman@pear.vc",
    "mar@pear.vc",
    "brett@initialized.com",
    "charles@precursorvc.com",
    "vivjan@hyperplane.vc",
    "roy@bloombergbeta.com",
    "james@bloombergbeta.com",
    "chris@fuelcapital.com",
    "leah@fuelcapital.com",
    "bucky@lsvp.com",
    "arj@tribecap.co",
    "aydin@felicis.com",
    "brandon.reeves@luxcapital.com",
    "grace.isford@luxcapital.com",
    "ethan@chemistry.vc",
    "drew@firststar.vc",
    "greg@costanoavc.com",
    "john@costanoavc.com",
    "ali@outsetcapital.com",
    "peter@wing.vc",
    "sara@wave.capital"
]

print(f"Testing {len(test_emails)} investor emails via parallel SMTP...")
results = verify_emails_parallel(test_emails, max_workers=10)
for email, res in results.items():
    print(f"{email} -> status: {res.get('status')}, code: {res.get('smtp_code')}, catchall: {res.get('is_catchall')}")
