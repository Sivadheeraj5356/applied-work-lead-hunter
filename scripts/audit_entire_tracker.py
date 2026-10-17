import csv
import os
import json
from collections import Counter

data_dir = r"C:\Users\E-siva-dheeraj\applied-work\tracker_data"
exports_dir = r"C:\Users\E-siva-dheeraj\applied-work\exports"
os.makedirs(exports_dir, exist_ok=True)

# 1. Analyze Data tab (156275556)
data_file = os.path.join(data_dir, "Data_156275556.csv")
with open(data_file, "r", encoding="utf-8", errors="ignore") as f:
    data_lines = f.readlines()

print(f"Data tab lines: {len(data_lines)}")
# Header is at row 15 (index 14)
data_header = [c.strip() for c in next(csv.reader([data_lines[14]]))]
print("Data tab header:", data_header)

data_rows = []
for line in data_lines[15:]:
    if line.strip():
        try:
            row = next(csv.reader([line]))
            if row and row[0].strip() and not row[0].startswith("="):
                data_rows.append(row)
        except Exception:
            pass

print(f"Data valid account rows: {len(data_rows)}")

# 2. Analyze Data Brokering tab (1346198609)
db_file = os.path.join(data_dir, "Data_Brokering_1346198609.csv")
with open(db_file, "r", encoding="utf-8", errors="ignore") as f:
    db_lines = f.readlines()
print(f"Data Brokering lines: {len(db_lines)}")
db_rows = []
for line in db_lines[15:]:
    if line.strip():
        try:
            row = next(csv.reader([line]))
            if row and row[0].strip() and not row[0].startswith("="):
                db_rows.append(row)
        except Exception:
            pass
print(f"Data Brokering valid account rows: {len(db_rows)}")

# 3. Analyze Compute Brokering tab (1773397198)
cb_file = os.path.join(data_dir, "Compute_Brokering_1773397198.csv")
with open(cb_file, "r", encoding="utf-8", errors="ignore") as f:
    cb_lines = f.readlines()
print(f"Compute Brokering lines: {len(cb_lines)}")
cb_rows = []
for line in cb_lines[15:]:
    if line.strip():
        try:
            row = next(csv.reader([line]))
            if row and row[0].strip() and not row[0].startswith("="):
                cb_rows.append(row)
        except Exception:
            pass
print(f"Compute Brokering valid account rows: {len(cb_rows)}")

# 4. Analyze linkeldn tab (910004)
link_file = os.path.join(data_dir, "linkeldn_910004.csv")
with open(link_file, "r", encoding="utf-8", errors="ignore") as f:
    link_rows = list(csv.DictReader(f))
print(f"linkeldn rows: {len(link_rows)}")

# 5. Analyze Daily Signals tab (910006)
signals_file = os.path.join(data_dir, "Daily_Signals_910006.csv")
with open(signals_file, "r", encoding="utf-8", errors="ignore") as f:
    signals_rows = list(csv.DictReader(f))
print(f"Daily Signals rows: {len(signals_rows)}")

# 6. Analyze Email Enrichment Queue (910007)
enrich_file = os.path.join(data_dir, "Email_Enrichment_Queue_910007.csv")
with open(enrich_file, "r", encoding="utf-8", errors="ignore") as f:
    enrich_rows = list(csv.DictReader(f))
print(f"Email Enrichment Queue rows: {len(enrich_rows)}")

summary = {
    "total_tabs": 10,
    "accounts_by_lane": {
        "Data (Raja)": len(data_rows),
        "Data Brokering (Hasan)": len(db_rows),
        "Compute Brokering (Alina)": len(cb_rows)
    },
    "linkedin_leads_tab_910004": len(link_rows),
    "daily_signals_tab_910006": len(signals_rows),
    "enrichment_queue_tab_910007": len(enrich_rows)
}

with open(os.path.join(exports_dir, "tracker_deep_audit.json"), "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("\nTracker analysis complete! Saved to tracker_deep_audit.json")
