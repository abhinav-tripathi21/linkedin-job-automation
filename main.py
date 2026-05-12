from linkedin_scraper import search_jobs
from gmail_service import send_email

jobs = search_jobs("Java Developer")

for job in jobs:

    subject = f"Application for {job['title']}"

    body = f"""
Hello Hiring Team,

I am interested in the {job['title']} role at {job['company']}.

Please find my resume attached.

Regards,
NAME
"""

    send_email(
        receiver_email=job["email"],
        subject=subject,
        body=body,
        resume_path="resumes/resume.pdf"
    )