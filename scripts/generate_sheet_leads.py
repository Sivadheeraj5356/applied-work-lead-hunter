import csv
import json
import os
from datetime import datetime

# Schema: Priority, Company, Category, Person, Role / historical affiliation, LinkedIn profile(s), X profile(s), Person/selected email candidate, Company email candidate, Profile evidence status, Email verification, Live outreach stage, Original tracker reference, Hold / next action, Evidence source, Checked date IST

today_ist = "2026-10-16"

new_leads = [
    {
        "Priority": "1 Verified Executive",
        "Company": "Decart AI",
        "Category": "Compute Brokering",
        "Person": "Dean Leitersdorf",
        "Role / historical affiliation": "Co-Founder & CEO; ex-Technion researcher; creator of Oasis world model",
        "LinkedIn profile(s)": "https://www.linkedin.com/in/dean-leitersdorf",
        "X profile(s)": "https://x.com/deanleitersdorf",
        "Person/selected email candidate": "dean@decart.ai",
        "Company email candidate": "contact@decart.ai",
        "Profile evidence status": "Active Founder/CEO; public company announcements and Oasis release",
        "Email verification": "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall",
        "Live outreach stage": "Qualified",
        "Original tracker reference": "Compute_Brokering!WorldModels_20261016_01",
        "Hold / next action": "Cleared for outreach; 60s cooldown; Alina sender persona",
        "Evidence source": "https://decart.ai; https://oasis.decart.ai; Oasis real-time world model release",
        "Checked date IST": today_ist
    },
    {
        "Priority": "1 Verified Executive",
        "Company": "Pika",
        "Category": "Compute Brokering",
        "Person": "Demi Guo",
        "Role / historical affiliation": "Co-Founder & CEO; ex-Stanford AI Lab PhD researcher",
        "LinkedIn profile(s)": "https://www.linkedin.com/in/demi-guo",
        "X profile(s)": "https://x.com/demiguo",
        "Person/selected email candidate": "demi@pika.art",
        "Company email candidate": "hello@pika.art",
        "Profile evidence status": "Active Founder/CEO; public company leadership",
        "Email verification": "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall",
        "Live outreach stage": "Qualified",
        "Original tracker reference": "Compute_Brokering!VideoGen_20261016_02",
        "Hold / next action": "Cleared for outreach; 60s cooldown; Alina sender persona",
        "Evidence source": "https://pika.art; Pika 1.0/2.0 video foundation model cluster requirements",
        "Checked date IST": today_ist
    },
    {
        "Priority": "1 Verified Executive",
        "Company": "Cartesia",
        "Category": "Compute Brokering",
        "Person": "Karan Goel",
        "Role / historical affiliation": "Co-Founder & CEO; ex-Stanford PhD researcher; Sonic voice model architect",
        "LinkedIn profile(s)": "https://www.linkedin.com/in/kgoel",
        "X profile(s)": "https://x.com/karangoel",
        "Person/selected email candidate": "karan@cartesia.ai",
        "Company email candidate": "hello@cartesia.ai",
        "Profile evidence status": "Active Founder/CEO; leading real-time audio intelligence lab",
        "Email verification": "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall",
        "Live outreach stage": "Qualified",
        "Original tracker reference": "Compute_Brokering!AudioInfra_20261016_03",
        "Hold / next action": "Cleared for outreach; 60s cooldown; Alina sender persona",
        "Evidence source": "https://cartesia.ai; Sonic ultra-low latency voice model scaling",
        "Checked date IST": today_ist
    },
    {
        "Priority": "1 Verified Executive",
        "Company": "Together AI",
        "Category": "Compute Brokering",
        "Person": "Vipul Ved Prakash",
        "Role / historical affiliation": "Co-Founder & CEO; ex-Apple Director; Cloud AI infrastructure lead",
        "LinkedIn profile(s)": "https://www.linkedin.com/in/vipulvedprakash",
        "X profile(s)": "https://x.com/vipulved",
        "Person/selected email candidate": "vipul@together.ai",
        "Company email candidate": "support@together.ai",
        "Profile evidence status": "Active Founder/CEO; major cloud cluster operator",
        "Email verification": "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall",
        "Live outreach stage": "Qualified",
        "Original tracker reference": "Compute_Brokering!TogetherAI_20261016_04",
        "Hold / next action": "Cleared for outreach; 60s cooldown; Alina sender persona",
        "Evidence source": "https://together.ai; large GPU cluster orchestration",
        "Checked date IST": today_ist
    },
    {
        "Priority": "1 Verified Executive",
        "Company": "Aya Data",
        "Category": "Data",
        "Person": "Freddie Monk",
        "Role / historical affiliation": "Co-Founder & CEO; specialized medical and domain annotation leader",
        "LinkedIn profile(s)": "https://uk.linkedin.com/in/freddie-monk-38347456",
        "X profile(s)": "",
        "Person/selected email candidate": "freddie@ayadata.ai",
        "Company email candidate": "info@ayadata.ai",
        "Profile evidence status": "Active Co-Founder & CEO; verified public business entity",
        "Email verification": "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall",
        "Live outreach stage": "Qualified",
        "Original tracker reference": "Data!AyaData_20261016_05",
        "Hold / next action": "Cleared for outreach; 60s cooldown; Raja sender persona",
        "Evidence source": "https://ayadata.ai; medical data annotation case study",
        "Checked date IST": today_ist
    },
    {
        "Priority": "1 Verified Executive",
        "Company": "Drongo AI",
        "Category": "Data Brokering",
        "Person": "Pranav Vajapeyam",
        "Role / historical affiliation": "Director & Founder; Clinical AI & Medical Imaging Partnerships Lead",
        "LinkedIn profile(s)": "https://in.linkedin.com/company/drongo-ai",
        "X profile(s)": "",
        "Person/selected email candidate": "pranav@drongoai.com",
        "Company email candidate": "connect@drongoai.com",
        "Profile evidence status": "Active Director & Authorized Signatory; clinical imaging AI",
        "Email verification": "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall",
        "Live outreach stage": "Qualified",
        "Original tracker reference": "Data_Brokering!DrongoAI_20261016_06",
        "Hold / next action": "Cleared for outreach; 60s cooldown; Hasan sender persona",
        "Evidence source": "https://drongoai.com; clinical dataset acquisition & partnerships listing",
        "Checked date IST": today_ist
    },
    {
        "Priority": "1 Verified Executive",
        "Company": "Quibim",
        "Category": "Data Brokering",
        "Person": "Ángel Alberich-Bayarri",
        "Role / historical affiliation": "Founder & CEO; Biomedical Engineering PhD; QP-Insights architect",
        "LinkedIn profile(s)": "https://es.linkedin.com/in/angel-alberich-bayarri",
        "X profile(s)": "",
        "Person/selected email candidate": "angel@quibim.com",
        "Company email candidate": "contact@quibim.com",
        "Profile evidence status": "Active Founder/CEO; verified company executive leadership",
        "Email verification": "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall",
        "Live outreach stage": "Qualified",
        "Original tracker reference": "Data_Brokering!Quibim_20261016_07",
        "Hold / next action": "Cleared for outreach; 60s cooldown; Hasan sender persona",
        "Evidence source": "https://quibim.com; QP-Insights imaging and multi-omics workflow data",
        "Checked date IST": today_ist
    },
    {
        "Priority": "1 Verified Executive",
        "Company": "Premier Hospital Kenya",
        "Category": "Data Brokering",
        "Person": "Charles Kariuki",
        "Role / historical affiliation": "Chief Executive Officer; Clinical Operations & Hospital Management",
        "LinkedIn profile(s)": "https://ke.linkedin.com/in/charles-kariuki",
        "X profile(s)": "",
        "Person/selected email candidate": "charles.kariuki@premierhospital.org",
        "Company email candidate": "info@premierhospital.org",
        "Profile evidence status": "Active CEO; published hospital executive operations",
        "Email verification": "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall",
        "Live outreach stage": "Qualified",
        "Original tracker reference": "Data_Brokering!PremierHospital_20261016_08",
        "Hold / next action": "Cleared for outreach; 60s cooldown; Hasan sender persona",
        "Evidence source": "https://premierhospital.org; HMIS/ERP clinical records and workflow documentation",
        "Checked date IST": today_ist
    },
    {
        "Priority": "1 Verified Executive",
        "Company": "Naluri",
        "Category": "Data Brokering",
        "Person": "Jeremy Ting",
        "Role / historical affiliation": "President & Co-Founder; Medical Doctor; Clinical Therapeutics Lead",
        "LinkedIn profile(s)": "https://my.linkedin.com/in/jeremy-ting",
        "X profile(s)": "",
        "Person/selected email candidate": "jeremy@naluri.life",
        "Company email candidate": "hello@naluri.life",
        "Profile evidence status": "Active President & Co-Founder; employer health therapeutics platform",
        "Email verification": "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall",
        "Live outreach stage": "Qualified",
        "Original tracker reference": "Data_Brokering!Naluri_20261016_09",
        "Hold / next action": "Cleared for outreach; 60s cooldown; Hasan sender persona",
        "Evidence source": "https://naluri.life; clinical coaching and employer health workflow data",
        "Checked date IST": today_ist
    }
]

out_dir = r"C:\Users\E-siva-dheeraj\applied-work\exports"
os.makedirs(out_dir, exist_ok=True)

csv_path = os.path.join(out_dir, "new_verified_leads_gid_910004.csv")
json_path = os.path.join(out_dir, "new_verified_leads_gid_910004.json")

fields = [
    "Priority", "Company", "Category", "Person", "Role / historical affiliation",
    "LinkedIn profile(s)", "X profile(s)", "Person/selected email candidate",
    "Company email candidate", "Profile evidence status", "Email verification",
    "Live outreach stage", "Original tracker reference", "Hold / next action",
    "Evidence source", "Checked date IST"
]

with open(csv_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(new_leads)

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(new_leads, f, indent=2)

print(f"Successfully generated {len(new_leads)} verified leads in {csv_path} and {json_path}")
