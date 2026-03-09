from apscheduler.schedulers.blocking import BlockingScheduler
from fetcher import fetch_new_articles
from summarizer import summarize_articles
from notifier import send_email
from datetime import datetime


def run_agent():
    """Main pipeline: fetch → summarize → notify."""
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running news agent...")

    articles = fetch_new_articles()

    if not articles:
        print("No new articles found. Skipping email.")
        return

    digest = summarize_articles(articles)
    send_email(digest)
    print("Done!\n")


if __name__ == "__main__":
    print("🤖 News Agent starting up...")

    # Run once immediately on startup
    run_agent()

    # Then schedule to run every hour
    scheduler = BlockingScheduler()
    scheduler.add_job(run_agent, "interval", hours=1)

    print("⏰ Scheduler running — agent will check for news every hour.")
    print("   Press Ctrl+C to stop.\n")

    try:
        scheduler.start()
    except KeyboardInterrupt:
        print("\nAgent stopped.")