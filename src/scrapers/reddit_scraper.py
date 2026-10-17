"""
Reddit Community Signal Scanner
Monitors targeted subreddits (r/LocalLLaMA, r/MachineLearning, r/sysadmin, r/startups)
for unfulfilled compute capacity demands, dataset sourcing requests, and startup wind-down signals.
"""

import requests
import json

class RedditSignalScanner:
    def __init__(self):
        self.subreddits = ["LocalLLaMA", "MachineLearning", "startups", "sysadmin"]
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    def scan_subreddit(self, subreddit, query="compute OR GPU OR dataset OR licensing", limit=25):
        """Fetches search posts from Reddit public JSON feeds."""
        url = f"https://www.reddit.com/r/{subreddit}/search.json?q={query}&restrict_sr=1&sort=new&limit={limit}"
        try:
            resp = requests.get(url, headers=self.headers, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                posts = []
                for child in data.get("data", {}).get("children", []):
                    d = child.get("data", {})
                    posts.append({
                        "id": d.get("id"),
                        "title": d.get("title"),
                        "selftext": d.get("selftext", "")[:300],
                        "author": d.get("author"),
                        "url": f"https://reddit.com{d.get('permalink')}",
                        "created_utc": d.get("created_utc"),
                        "subreddit": subreddit
                    })
                return posts
        except Exception:
            pass
        return []
