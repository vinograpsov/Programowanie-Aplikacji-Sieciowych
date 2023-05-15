import smtplib
from email import encoders
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64

def sent_email_with_image(from_email, to_email, subject, mess, image_path):
    
    msg = MIMEMultipart()
    msg["From"] - from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(mess, 'plain'))

    with open(image_path, "rb") as f:
        image_data = f.read()

    encoded_image_data = base64.b64encode(image_data).decode("utf-8")
    image = MIMEImage(base64.b64decode(encoded_image_data))
    image.add_header("Content-Disposition", f"attachment; filename = {image_path}")
    msg.attach(image)

    server = smtplib.SMTP("interia.pl", 587)
    server.starttls()
    server.login(from_email, "P4SInf2017")
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()


from_email = "pas2017@interia.pl"
to_email = "pas2017@interia.pl"
subject = "test zad1"
mess = "mess zad1"
file_path = "test.png"

sent_email_with_image(from_email, to_email, subject, mess, file_path)