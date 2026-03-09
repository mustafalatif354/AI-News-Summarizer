import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into the environment

# ─── Secrets (loaded from .env) ──────────────────────────────────────────────
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# ─── News Agent Configuration ────────────────────────────────────────────────

# RSS feeds to monitor
FEEDS = [
    "https://rss.app/feeds/T0Cpow1r7qYBvXtc.xml",
    "https://rss.app/feeds/IxbBh8pbiIY23xb5.xml"
]

# How many recent articles to summarize per feed per run
MAX_ARTICLES_PER_FEED = 5

# Claude model to use
CLAUDE_MODEL = "claude-haiku-4-5-20251001"  # fast + cheap, great for summarization