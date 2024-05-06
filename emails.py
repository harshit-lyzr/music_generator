import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_emails(sender_email, receiver_email, subject, body_message, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body message
    message.attach(MIMEText(body_message, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())


def send_email(rec_email):
    sender_email = "harshilnariya7422@gmail.com"
    receiver_email = rec_email
    subject = "Lyzr Music Generation Completed!!"
    body_message = f"""Hello User,

    Thanks For Using Lyzr Music Generator.
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    smtp_username = "harshilnariya7422@gmail.com"
    smtp_password = "qeyb shss cbxx xaam"

    send_emails(sender_email, receiver_email, subject, body_message, smtp_server, smtp_port, smtp_username, smtp_password)
