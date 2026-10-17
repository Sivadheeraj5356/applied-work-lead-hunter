import csv

def inspect_summary(path, name):
    print(f"=== {name} ===")
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        reader = list(csv.reader(f))
        for row in reader[:35]:
            # print non-empty rows
            non_empty = [c for c in row if c.strip()]
            if non_empty:
                print(" | ".join(row[:8]))
    print()

inspect_summary(r'C:\Users\E-siva-dheeraj\applied-work\tracker_data\Data_Summary_910001.csv', 'DATA SUMMARY')
inspect_summary(r'C:\Users\E-siva-dheeraj\applied-work\tracker_data\Data_Brokering_Summary_910002.csv', 'DATA BROKERING SUMMARY')
inspect_summary(r'C:\Users\E-siva-dheeraj\applied-work\tracker_data\Compute_Brokering_Summary_910003.csv', 'COMPUTE BROKERING SUMMARY')
