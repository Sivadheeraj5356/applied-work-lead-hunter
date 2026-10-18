import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.check_blacklist_helper import normalize, norm_set

# Let's inspect the blacklist for compute names
print("Sample blacklisted compute items:")
count = 0
for b in sorted(list(norm_set)):
    if any(k in b for k in ['compute', 'cloud', 'ai', 'cluster', 'labs']):
        print(" ", b)
        count += 1
        if count >= 30:
            break
