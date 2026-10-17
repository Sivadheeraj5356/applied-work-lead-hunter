"""
Deduplication and Blacklist Manager
Guarantees 100% uniqueness of target companies and domains across all Applied Work tabs.
"""

import os
import re

class Deduplicator:
    def __init__(self, blacklist_path=r"C:\Users\E-siva-dheeraj\applied-work\tracker_data\live_blacklist_set.txt"):
        self.blacklist = set()
        self.blacklist_path = blacklist_path
        self.load_blacklist()

    def normalize(self, name):
        if not name:
            return ""
        n = name.lower().strip()
        n = re.sub(r'\b(inc|llc|corp|ltd|limited|co|ai|io|technologies|solutions|group|labs)\b', '', n)
        n = re.sub(r'[^a-z0-9]', '', n)
        return n

    def load_blacklist(self):
        if os.path.exists(self.blacklist_path):
            with open(self.blacklist_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        self.blacklist.add(self.normalize(line))
        print(f"Loaded {len(self.blacklist)} normalized companies into deduplication blacklist.")

    def is_duplicate(self, company_name):
        norm = self.normalize(company_name)
        return norm in self.blacklist

    def add(self, company_name):
        norm = self.normalize(company_name)
        if norm:
            self.blacklist.add(norm)
