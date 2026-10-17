"""
Public News & Corporate Filings Scanner
Ingests business articles, bankruptcy notices, SEC Chapter 11 filings, and tech funding releases.
"""

import requests
import xml.etree.ElementTree as ET

class NewsSignalScanner:
    def __init__(self):
        self.rss_sources = [
            ("TechCrunch AI", "https://techcrunch.com/category/artificial-intelligence/feed/"),
            ("PR Newswire Tech", "https://www.prnewswire.com/rss/technology-latest-news/technology-latest-news-list.rss"),
            ("Hacker News Top", "https://hnrss.org/frontpage")
        ]
        self.headers = {"User-Agent": "AppliedWorkBot/1.0"}

    def scan_rss_feed(self, url, limit=20):
        try:
            resp = requests.get(url, headers=self.headers, timeout=6)
            if resp.status_code == 200:
                root = ET.fromstring(resp.content)
                items = []
                for item in root.findall(".//item")[:limit]:
                    title = item.find("title").text if item.find("title") is not None else ""
                    link = item.find("link").text if item.find("link") is not None else ""
                    desc = item.find("description").text if item.find("description") is not None else ""
                    pubDate = item.find("pubDate").text if item.find("pubDate") is not None else ""
                    items.append({
                        "title": title,
                        "link": link,
                        "description": desc[:300] if desc else "",
                        "pubDate": pubDate
                    })
                return items
        except Exception:
            pass
        return []
