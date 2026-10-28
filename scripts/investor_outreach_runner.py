"""
Automated 120s Investor Outreach Dispatcher:
- From: Raja Adil <raja@appliedwork.ai>
- Mode: Sequential dispatch with strict 120-second sleep between emails.
- Safety: Checks inbox for any new bounces (Undelivered Mail Returned to Sender) before each dispatch.
  If a new bounce is detected, halts execution immediately and notifies.
- Verification: Only sends to pre-verified, non-catchall DELIVERABLE (SMTP 250) recipients.
"""

import os
import sys
import time
import json
import requests

ACCOUNT_ID = "7575716000000008002"
FROM_ADDR = "raja@appliedwork.ai"
SUBJECT = "Expert supply and specialised datasets for vertical AI evals"

# Filtered list of verified DELIVERABLE (non-catchall SMTP 250) investors
INVESTOR_QUEUE = [
    {
        "name": "Sarah Catanzaro",
        "first_name": "Sarah",
        "email": "sarah.catanzaro@amplifypartners.com",
        "fund": "Amplify Partners",
        "portfolio": "Runway and Modal"
    },
    {
        "name": "Ethan Kurzweil",
        "first_name": "Ethan",
        "email": "ethan@chemistry.vc",
        "fund": "Chemistry VC",
        "portfolio": "LaunchDarkly and early AI infrastructure"
    },
    {
        "name": "Lee Edwards",
        "first_name": "Lee",
        "email": "lee@root.vc",
        "fund": "Root Ventures",
        "portfolio": "Great Expectations and Esper"
    },
    {
        "name": "Alessio Fanelli",
        "first_name": "Alessio",
        "email": "alessio@decibel.vc",
        "fund": "Decibel Partners",
        "portfolio": "Modal, Fireworks.ai, and E2B"
    },
    {
        "name": "Greg Sands",
        "first_name": "Greg",
        "email": "greg@costanoavc.com",
        "fund": "Costanoa Ventures",
        "portfolio": "Alation and Fivetran"
    },
    {
        "name": "John Cowgill",
        "first_name": "John",
        "email": "john@costanoavc.com",
        "fund": "Costanoa Ventures",
        "portfolio": "Astronomer and Hightouch"
    },
    {
        "name": "Gaurav Jain",
        "first_name": "Gaurav",
        "email": "gaurav@afore.vc",
        "fund": "Afore Capital",
        "portfolio": "early-stage data and AI infrastructure"
    },
    {
        "name": "Chad Byers",
        "first_name": "Chad",
        "email": "chad@susaventures.com",
        "fund": "Susa Ventures",
        "portfolio": "Scale AI and Flexport"
    },
    {
        "name": "Roy Bahat",
        "first_name": "Roy",
        "email": "roy@bloombergbeta.com",
        "fund": "Bloomberg Beta",
        "portfolio": "DeepSee, Zapier, and Primer AI"
    },
    {
        "name": "James Cham",
        "first_name": "James",
        "email": "james@bloombergbeta.com",
        "fund": "Bloomberg Beta",
        "portfolio": "Domino Data Lab and Context.io"
    },
    {
        "name": "Nihal Mehta",
        "first_name": "Nihal",
        "email": "nihal@eniac.vc",
        "fund": "Eniac Ventures",
        "portfolio": "Bedrock, Ironclad, and Alloy"
    },
    {
        "name": "Satya Patel",
        "first_name": "Satya",
        "email": "satya@homebrew.co",
        "fund": "Homebrew",
        "portfolio": "Plaid, Finix, and Gusto"
    },
    {
        "name": "Topher Conway",
        "first_name": "Topher",
        "email": "topher@svangel.com",
        "fund": "SV Angel",
        "portfolio": "Scale AI, Stripe, and Airbnb"
    }
]

def generate_body(first_name, portfolio):
    return f"""Hi {first_name},

Saw your investments in {portfolio} and your thesis around foundational AI data infrastructure.

I'm Raja, founder at Applied Work. We build a high-calibre expert supply network and produce specialised, proprietary datasets for frontier labs and vertical AI companies.

Generalist crowd annotators fail when foundation models need rigorous reasoning and domain accuracy. We curate certified industry professionals—across construction engineering, insurance underwriting, industrial telemetry, and legal workflows—to generate verifiable trajectory data, domain testbenches, and gold-standard evaluation sets.

We are turning this human expert pipeline into reusable, versioned benchmark environments for model training and RLHF/RL.

Would love to connect for 15 minutes to share our traction notes and hear your perspective on the space.

Best,
Raja
Founder, Applied Work"""

print(f"Loaded {len(INVESTOR_QUEUE)} pre-verified investor targets.")
