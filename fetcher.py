import feedparser
import json
import os
from datetime import datetime
from config import FEEDS, MAX_ARTICLES_PER_FEED

# File to persist seen article URLs between runs
SEEN_ARTICLES_FILE = "seen_articles.json"


def load_seen_articles() -> set:
    """Load the set of already-seen article URLs from disk."""
    if os.path.exists(SEEN_ARTICLES_FILE):
        with open(SEEN_ARTICLES_FILE, "r") as f:
            return set(json.load(f))
    return set()


def save_seen_articles(seen: set):
    """Save the set of seen article URLs to disk."""
    with open(SEEN_ARTICLES_FILE, "w") as f:
        json.dump(list(seen), f)


def fetch_new_articles() -> list[dict]:
    """
    Fetch new articles from all configured RSS feeds.
    Returns a list of article dicts with title, summary, link, and source.
    """
    seen = load_seen_articles()
    new_articles = []

    for feed_url in FEEDS:
        print(f"Fetching: {feed_url}")
        feed = feedparser.parse(feed_url)
        source_name = feed.feed.get("title", feed_url)
        count = 0

        for entry in feed.entries:
            if count >= MAX_ARTICLES_PER_FEED:
                break

            url = entry.get("link", "")
            if not url or url in seen:
                continue

            new_articles.append({
                "title": entry.get("title", "No title"),
                "summary": entry.get("summary", entry.get("description", "")),
                "link": url,
                "source": source_name,
                "published": entry.get("published", str(datetime.now())),
            })

            seen.add(url)
            count += 1

    save_seen_articles(seen)
    print(f"Found {len(new_articles)} new articles.")
    return new_articles