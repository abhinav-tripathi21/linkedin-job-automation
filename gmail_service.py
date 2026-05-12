import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "EMAIL"
SENDER_PASSWORD = "linkedinautomated"

def send_email(receiver_email, subject, body, resume_path):

    msg = EmailMessage()

    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email

    msg.set_content(body)

    # Attach resume
    with open(resume_path, "rb") as file:

        file_data = file.read()

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="pdf",
            filename="resume.pdf"
        )

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(
            SENDER_EMAIL,
            SENDER_PASSWORD
        )

        smtp.send_message(msg)

    print("Email sent to:", receiver_email)