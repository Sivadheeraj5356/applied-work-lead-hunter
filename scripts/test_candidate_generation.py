import os
import sys
import re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.check_blacklist_helper import normalize, norm_set

# Let's verify our sources for each category
print("Verifying candidate generation engine...")
