import os

tabs = [
    ("Data (156275556)", r"C:\Users\E-siva-dheeraj\applied-work\tracker_data\Data_156275556.csv"),
    ("Data Brokering (1346198609)", r"C:\Users\E-siva-dheeraj\applied-work\tracker_data\Data_Brokering_1346198609.csv"),
    ("Compute Brokering (1773397198)", r"C:\Users\E-siva-dheeraj\applied-work\tracker_data\Compute_Brokering_1773397198.csv")
]

for title, path in tabs:
    print(f"\n========================================\n{title}\n========================================")
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for i in range(20):
            line = f.readline().strip()
            if line:
                print(f"L{i+1}: {line[:130]}")
