import yagmail
import datetime

def send_email_with_attachment(to_email, user, pdf_path):
    yag = yagmail.SMTP("email", "password")
    subject = "Your Enrollment File"
    body = f"""
    Dear {user.name},
    
    Attached is your enrollment file, downloaded on {datetime.datetime.now()}.

    Best Regards,
    Infostud API
    """
    yag.send(
        to=to_email,
        subject=subject,
        contents=body,
        attachments=pdf_path
        )
