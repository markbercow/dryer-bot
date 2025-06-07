import smtplib
from email.mime.text import MIMEText
import random
import logging
from app.config import config

messages = config['messages']
smtp_server = config['email']['smtp_server']
smtp_port = config['email']['smtp_port']
sender_email = config['email']['sender_email']
sender_password = config['email']['sender_password']
recipients = config['recipients']

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def text_dryer_done_email():
    selected_message = random.choice(messages[1:])
    msg = MIMEText(selected_message)
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = ""
    logging.info("Sending dryer done message.")
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipients, msg.as_string())
        logging.info("SMS messages sent!")
    except Exception as e:
        logging.error(f"Failed to send SMS: {e}")
