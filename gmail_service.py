import smtplib
import os

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

def send_email(receiver_email, subject, body, resume_path, cc_emails=None):

    try:

        msg = EmailMessage()

        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email

        if cc_emails:
            msg["Cc"] = ", ".join(cc_emails)

        msg.set_content(body)

        with open(resume_path, "rb") as file:

            file_data = file.read()

            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="pdf",
                filename="resume.pdf"
            )

        #receipients list
        all_recipients = [receiver_email]

        if cc_emails:
            all_recipients += cc_emails

        #print("3. Connecting Gmail")
        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
             465
        ) as smtp:

            smtp.login(
                SENDER_EMAIL,
                SENDER_PASSWORD
            )
            #print("5. Sending email")
            smtp.send_message(
                msg,
                to_addrs=all_recipients
            )

        print("6. Email sent successfully")

    except Exception as e:

        print("EMAIL ERROR:", e)
