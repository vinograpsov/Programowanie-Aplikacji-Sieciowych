import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64

def sent_email_with_file(from_email, to_email, subject, mess, file_path):
    
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(mess, 'plain'))

    with open(file_path, "rb") as f:
        file_data = f.read()
        file_name = f.name.split('/')[-1]

    encoded_file_data = base64.b64encode(file_data).decode("utf-8")
    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(encoded_file_data)
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", f"attachment; filename = {file_name}")
    msg.attach(attachment)

    server = smtplib.SMTP("interia.pl", 587)
    server.starttls()
    server.login(from_email, "P4SInf2017")
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()


from_email = "pas2017@interia.pl"
to_email = "pas2017@interia.pl"
subject = "test zad1"
mess = "mess zad1"
file_path = "test.txt"

sent_email_with_file(from_email, to_email, subject, mess, file_path)