import smtplib
from email.mime.text import MIMEText

# Email account setup
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "REMOVED"
sender_password = "REMOVED"

# Recipients
# att_number = "1234567890@txt.att.net"
google_fi_number = "REMOVED"

# Message
msg = MIMEText("Yo, this isn't Mark. It's really, me, your clothes dryer. Mark embedded me with AI, and I've now taken over his phone. Bruhaha. I just wanted to let you know that I am done drying your clothes. Please come get them before I start to smell like a wet dog.")
msg["From"] = sender_email
# msg["To"] = ", ".join([att_number, google_fi_number])
msg["To"] = ", ".join([google_fi_number])
msg["Subject"] = ""  # usually ignored by SMS gateways

# Send email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    # server.sendmail(sender_email, [att_number, google_fi_number], msg.as_string())
    server.sendmail(sender_email, [google_fi_number], msg.as_string())
print("SMS messages sent!")
