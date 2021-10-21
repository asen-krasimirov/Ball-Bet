import os
import smtplib
import ssl
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_contact_email(sender_email, message_content):
    middleware_email = os.getenv('MAIN_SENDER_EMAIL')
    middleware_pass = os.getenv('MAIN_SENDER_PASS')

    message = MIMEMultipart("alternative")
    message["Subject"] = f"Feedback Message"
    message["From"] = middleware_email
    message["To"] = middleware_email

    send_time = datetime.now().strftime("%H:%M:%S %b, %d, %Y")

    text_content = f"""
<br>
    <h2> A feedback message have just been received! </h2>
<p>
The message was send by {sender_email}
<br><br>
Message's content:\n
{message_content}
</p>
<br>
<time>Send on {send_time}</time>
"""

    text = MIMEText(text_content, "html")

    message.attach(text)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        try:
            server.login(middleware_email, middleware_pass)
            server.sendmail(
                middleware_email, middleware_email, message.as_string()
            )
            is_send_successfully = True

        except smtplib.SMTPAuthenticationError:
            is_send_successfully = False

    return is_send_successfully
