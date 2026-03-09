import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER


def send_email(digest: str):
    """
    Sends the news digest as an email via Gmail SMTP.
    """
    if not digest or digest == "No new articles to summarize.":
        print("Nothing to send.")
        return

    # Build the email
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"📰 News Digest — {datetime.now().strftime('%b %d, %Y %H:%M')}"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    # Plain text version
    text_part = MIMEText(digest, "plain")

    # HTML version (wraps the digest in simple formatting)
    html_body = f"""
    <html>
      <body style="font-family: Arial, sans-serif; max-width: 650px; margin: auto; padding: 20px;">
        <h2 style="color: #333;">📰 Your Hourly News Digest</h2>
        <p style="color: #888; font-size: 13px;">{datetime.now().strftime('%A, %B %d, %Y at %H:%M')}</p>
        <hr style="border: none; border-top: 1px solid #eee;" />
        <pre style="white-space: pre-wrap; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6;">
{digest}
        </pre>
        <hr style="border: none; border-top: 1px solid #eee;" />
        <p style="color: #aaa; font-size: 12px;">Sent by your News Agent 🤖</p>
      </body>
    </html>
    """
    html_part = MIMEText(html_body, "html")

    # Attach both versions (email clients will use HTML if supported)
    msg.attach(text_part)
    msg.attach(html_part)

    # Send via Gmail SMTP
    print("Sending email...")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

    print(f"Email sent to {EMAIL_RECEIVER} ✓")