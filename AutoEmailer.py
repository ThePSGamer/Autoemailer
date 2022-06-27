import smtplib
import ssl
import os
from email.message import EmailMessage

# These two lines pull the email and password from envirnment variables that were previously set up
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()

# body of your message goes here
msg.set_content(
    "")
# subject of your message goes here
msg["Subject"] = ""

msg["From"] = EMAIL_ADDRESS

# reciever of your email goes here
msg["To"] = ""

context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
    smtp.starttls(context=context)
    smtp.login(msg["From"], EMAIL_PASSWORD)
    smtp.send_message(msg)
