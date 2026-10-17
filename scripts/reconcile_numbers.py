# Reconcile exact numbers before and after insertion

current = {
    'Compute Brokering': {'total_rows': 418, 'unique_companies': 415, 'open_opps': 158},
    'Data': {'total_rows': 452, 'unique_companies': 451, 'open_opps': 167},
    'Data Brokering': {'total_rows': 495, 'unique_companies': 495, 'open_opps': 160}
}

# Batch 1 (150 Batch):
# Compute: 50
# Data: 50
# Data Brokering: 50

# Batch 2 (50 Data Batch):
# Data: 36
# Data Brokering: 14

compute_new = 50
data_new = 50 + 36 # 86
db_new = 50 + 14   # 64

print(f"Compute Brokering: {current['Compute Brokering']['total_rows']} -> {current['Compute Brokering']['total_rows'] + compute_new} rows (+{compute_new})")
print(f"Data: {current['Data']['total_rows']} -> {current['Data']['total_rows'] + data_new} rows (+{data_new})")
print(f"Data Brokering: {current['Data Brokering']['total_rows']} -> {current['Data Brokering']['total_rows'] + db_new} rows (+{db_new})")
print(f"Combined Total New Rows: {compute_new + data_new + db_new} novel leads across 2 batches")
