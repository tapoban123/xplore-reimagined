from app.utils.constants import GMAIL_CREDS, OTP_TYPE
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from .otp_templates import (
    LOG_IN_OTP_TEMPLATE,
    SIGN_UP_OTP_TEMPLATE,
    RESET_PASSWORD_OTP_TEMPLATE,
)


def send_mail(otp: int, otp_type: OTP_TYPE, receiver_email: str) -> None:
    """Function that creates an email message and sends to the provided gmail inbox."""
    SENDER_EMAIL = "xplore541@gmail.com"
    RECEIVER_EMAIL = receiver_email
    PASSWORD = GMAIL_CREDS.APP_PASSWORD

    subject = ""
    html_body = ""

    if otp_type == OTP_TYPE.SIGN_IN:
        subject = "Xplore - Your Sign In OTP"
        html_body = LOG_IN_OTP_TEMPLATE(otp)
    elif otp_type == OTP_TYPE.SIGN_UP:
        subject = "Xplore - Your Sign Up OTP"
        html_body = SIGN_UP_OTP_TEMPLATE(otp)
    else:
        subject = "Xplore - Password Reset Request OTP"
        html_body = RESET_PASSWORD_OTP_TEMPLATE(otp)

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["To"] = RECEIVER_EMAIL
    message["From"] = SENDER_EMAIL

    body = MIMEText(html_body, "html")

    message.attach(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
