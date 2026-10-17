import re

with open(r"C:\Users\E-siva-dheeraj\applied-work\tracker_data\Data_156275556.csv", "r", encoding="utf-8", errors="ignore") as f:
    lines = [f.readline() for _ in range(25)]

print("=== First 25 lines of Data (gid: 156275556) ===")
for i, l in enumerate(lines):
    if l.strip():
        print(f"L{i+1}: {l.strip()[:140]}")
