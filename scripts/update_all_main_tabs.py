import csv
import os

tracker_dir = r"C:\Users\E-siva-dheeraj\applied-work\tracker_data"
exports_dir = r"C:\Users\E-siva-dheeraj\applied-work\exports"

# 1. Update Compute Brokering (1773397198)
cb_in = os.path.join(tracker_dir, "Compute_Brokering_1773397198.csv")
cb_out = os.path.join(exports_dir, "Compute_Brokering_1773397198_updated.csv")

new_cb_leads = [
    ["Decart AI", "Dean Leitersdorf", "Co-Founder & CEO", "dean@decart.ai", "https://decart.ai; https://oasis.decart.ai", "Buyer", "Real-time world model inference & training GPU clusters", "Qualified", "", "", "", "Cleared for outreach; 60s cooldown; Alina", "", "", "", "", "", "Oasis real-time world model release", "contact@decart.ai", "dean@decart.ai", "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall", "Context: 2026", "1 Verified Executive", "alina@appliedwork.ai", "APPROVED", ""],
    ["Pika", "Demi Guo", "Co-Founder & CEO", "demi@pika.art", "https://pika.art", "Buyer", "Generative video foundation model training clusters", "Qualified", "", "", "", "Cleared for outreach; 60s cooldown; Alina", "", "", "", "", "", "Pika 1.0/2.0 video model scaling", "hello@pika.art", "demi@pika.art", "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall", "Context: 2026", "1 Verified Executive", "alina@appliedwork.ai", "APPROVED", ""],
    ["Cartesia", "Karan Goel", "Co-Founder & CEO", "karan@cartesia.ai", "https://cartesia.ai", "Buyer", "Sonic ultra-low latency voice foundation model GPU clusters", "Qualified", "", "", "", "Cleared for outreach; 60s cooldown; Alina", "", "", "", "", "", "Sonic voice model scaling", "hello@cartesia.ai", "karan@cartesia.ai", "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall", "Context: 2026", "1 Verified Executive", "alina@appliedwork.ai", "APPROVED", ""],
    ["Together AI", "Vipul Ved Prakash", "Co-Founder & CEO", "vipul@together.ai", "https://together.ai", "Partner", "Cloud AI infrastructure & GPU cluster orchestration", "Qualified", "", "", "", "Cleared for outreach; 60s cooldown; Alina", "", "", "", "", "", "Large GPU cluster scaling", "support@together.ai", "vipul@together.ai", "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall", "Context: 2026", "1 Verified Executive", "alina@appliedwork.ai", "APPROVED", ""]
]

with open(cb_in, "r", encoding="utf-8", errors="ignore") as f:
    cb_content = f.read()

with open(cb_out, "w", encoding="utf-8", newline="") as f:
    f.write(cb_content.rstrip())
    f.write("\n")
    writer = csv.writer(f)
    writer.writerows(new_cb_leads)

# 2. Update Data (156275556)
d_in = os.path.join(tracker_dir, "Data_156275556.csv")
d_out = os.path.join(exports_dir, "Data_156275556_updated.csv")

new_d_leads = [
    ["Aya Data", "Freddie Monk", "Co-Founder & CEO", "freddie@ayadata.ai", "https://ayadata.ai", "Supplier", "Medical data annotation & multi-lingual human QA pilots", "Qualified", "", "", "", "Cleared for outreach; 60s cooldown; Raja", "", "", "", "", "", "Medical data sourcing case study", "info@ayadata.ai", "freddie@ayadata.ai", "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall", "Context: 2026", "1 Verified Executive", "raja@appliedwork.ai", "APPROVED", ""]
]

with open(d_in, "r", encoding="utf-8", errors="ignore") as f:
    d_content = f.read()

with open(d_out, "w", encoding="utf-8", newline="") as f:
    f.write(d_content.rstrip())
    f.write("\n")
    writer = csv.writer(f)
    writer.writerows(new_d_leads)

# 3. Update Data Brokering (1346198609)
db_in = os.path.join(tracker_dir, "Data_Brokering_1346198609.csv")
db_out = os.path.join(exports_dir, "Data_Brokering_1346198609_updated.csv")

new_db_leads = [
    ["Drongo AI", "Pranav Vajapeyam", "Director & Founder", "pranav@drongoai.com", "https://drongoai.com", "Supplier", "Clinical dataset requirements & medical imaging workflow data", "Qualified", "", "", "", "Cleared for outreach; 60s cooldown; Hasan", "", "", "", "", "", "Clinical Data Partnerships Lead listing", "connect@drongoai.com", "pranav@drongoai.com", "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall", "Context: 2026", "1 Verified Executive", "hasan@appliedwork.ai", "APPROVED", ""],
    ["Quibim", "Ángel Alberich-Bayarri", "Founder & CEO", "angel@quibim.com", "https://quibim.com", "Supplier", "QP-Insights imaging and multi-omics workflow data licensing", "Qualified", "", "", "", "Cleared for outreach; 60s cooldown; Hasan", "", "", "", "", "", "QP-Insights clinical imaging platform", "contact@quibim.com", "angel@quibim.com", "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall", "Context: 2026", "1 Verified Executive", "hasan@appliedwork.ai", "APPROVED", ""],
    ["Premier Hospital Kenya", "Charles Kariuki", "Chief Executive Officer", "charles.kariuki@premierhospital.org", "https://premierhospital.org", "Supplier", "HMIS/ERP clinical enterprise systems workflow data", "Qualified", "", "", "", "Cleared for outreach; 60s cooldown; Hasan", "", "", "", "", "", "Official HMIS/ERP clinical documentation", "info@premierhospital.org", "charles.kariuki@premierhospital.org", "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall", "Context: 2026", "1 Verified Executive", "hasan@appliedwork.ai", "APPROVED", ""],
    ["Naluri", "Jeremy Ting", "President & Co-Founder", "jeremy@naluri.life", "https://naluri.life", "Supplier", "Digital therapeutics & employee health management workflow data", "Qualified", "", "", "", "Cleared for outreach; 60s cooldown; Hasan", "", "", "", "", "", "Clinical therapeutics coaching workflows", "hello@naluri.life", "jeremy@naluri.life", "SMTP_DELIVERABLE_250_OK; direct port 25 handshake confirmed; non-catchall", "Context: 2026", "1 Verified Executive", "hasan@appliedwork.ai", "APPROVED", ""]
]

with open(db_in, "r", encoding="utf-8", errors="ignore") as f:
    db_content = f.read()

with open(db_out, "w", encoding="utf-8", newline="") as f:
    f.write(db_content.rstrip())
    f.write("\n")
    writer = csv.writer(f)
    writer.writerows(new_db_leads)

print("Successfully written updated CSVs for all three main operational tabs!")
