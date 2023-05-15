import smtplib

# pas2017@interia.pl
# P4SInf2017

def send_email(from_email, to_email, subject, mess):
    server = smtplib.SMTP("interia.pl", 587)
    server.starttls()
    server.login(from_email, "P4SInf2017")

    msg = f"Subject: {subject}\n\n{mess}"
    server.sendmail(from_email, to_email, msg)
    server.quit()


from_email = "pas2017@interia.pl"
to_email = "pas2017@interia.pl"
subject = "test zad1"
mess = "mess zad1"

send_email(from_email, to_email, subject, mess)