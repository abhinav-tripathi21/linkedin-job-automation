def generate_email(job):

    subject = f"Application for {job['title']}"

    body = f"""
Dear Hiring Manager,

I am interested in the {job['title']} role at {job['company']}.

Please find my resume attached.

Regards,
Abhinav Tripathi
"""

    return subject, body