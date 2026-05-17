from linkedin_scraper import search_jobs
from gmail_service import send_email
import pandas as pd
from datetime import datetime
from email_template import generate_email

keywords = [
    "Java Developer C2C",
    "Business Analyst C2C",
    "Project Manager C2C",
    "Data Analyst C2C"
]

already_sent = set()

for keyword in keywords:

    print("Searching for ", keyword)

    jobs = search_jobs(keyword)

    df = pd.DataFrame(jobs)
    df.to_csv("data/jobs.csv", index=False)

    for job in jobs:

        print("JOB FOUND:", job)

        job["applied_at"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        subject, body = generate_email(job)

        if job["email"] not in already_sent:

            print("Sending email to:", job["email"])
            print(subject)
            print(body)

            send_email(
                receiver_email=job["email"],
                subject=subject,
                body=body,
                resume_path="resumes/resume.pdf",
                cc_emails=[
                    "quin@jpitstaffing.com",
                    "kim@jpitstaffing.com"
                ]
            )

            already_sent.add(job["email"])

            print("EMAIL SENT SUCCESSFULLY")

        else:
            print("DUPLICATE EMAIL SKIPPED:", job["email"])

print("\nALL APPLICATIONS SENT")
