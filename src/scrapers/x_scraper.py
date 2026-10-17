"""
X (Twitter) Intent & Signal Scanner
Scans X queries for AI GPU cluster needs, model scaling bottlenecks, dataset licensing RFPs,
and company pivots/layoffs using Twikit and open endpoint parsing.
"""

import re
import urllib.parse
import json

class XSignalScanner:
    def __init__(self):
        self.search_templates = [
            '("H100" OR "H200" OR "B200") ("looking for" OR "cluster" OR "capacity" OR "compute")',
            '("training data" OR "RLHF" OR "data licensing" OR "benchmark") ("seeking" OR "vendor" OR "hiring")',
            '("shuttering" OR "liquidating" OR "winding down" OR "assets for sale") ("AI" OR "startup" OR "data")'
        ]

    def build_search_url(self, query):
        encoded = urllib.parse.quote(query)
        return f"https://x.com/search?q={encoded}&f=live"

    def parse_tweet_signal(self, text, author, url):
        """Extracts structured intent from a tweet."""
        is_compute = any(k in text.lower() for k in ["h100", "h200", "b200", "cluster", "gpu", "inference"])
        is_data = any(k in text.lower() for k in ["dataset", "rlhf", "annotation", "data licensing", "benchmark"])
        is_distressed = any(k in text.lower() for k in ["winding down", "shuttering", "liquidat", "administration", "bankruptcy"])
        
        category = "Data Brokering" if is_distressed else ("Compute Brokering" if is_compute else "Data")
        
        return {
            "source": "X (Twitter)",
            "author": author,
            "url": url,
            "text": text,
            "category": category,
            "orientation": "Buyer" if "looking for" in text.lower() or "need" in text.lower() else "Supplier"
        }
