from playwright.sync_api import sync_playwright
from urllib.parse import quote
import os
from dotenv import load_dotenv
#import re
load_dotenv()

LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
def search_jobs(keyword):

    jobs = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        # Login
        page.goto("https://www.linkedin.com/login")

        page.fill("#username", "LINKEDIN_EMAIL")
        page.fill("#password", "LINKEDIN_PASSWORD")

        page.click("button[type='submit']")

        page.wait_for_timeout(5000)

        print("Logged into LinkedIn")

        # Search jobs
        encoded_keyword = quote(keyword)

        jobs_url = f"https://www.linkedin.com/jobs/search/?keywords={encoded_keyword}"

        page.goto(jobs_url)

        page.wait_for_timeout(5000)

        print("Jobs page opened")

        # Extract job titles
        titles = page.locator(".job-card-list__title").all_inner_texts()

        # Extract company names
        companies = page.locator(".job-card-container__company-name").all_inner_texts()

        # Store jobs
        for i in range(min(len(titles), len(companies))):

            job = {
                "title": titles[i],
                "company": companies[i]
            }

            jobs.append(job)

        browser.close()

    return jobs
