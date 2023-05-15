import smtplib

# pas2017@interia.pl
# P4SInf2017

def send_email(from_email, to_email, subject, mess):
    server = smtplib.SMTP("interia.pl", 587)
    server.starttls()
    server.login(from_email, input("enter your password: "))

    msg = f"Subject: {subject}\n\n{mess}"
    server.sendmail(from_email, to_email, msg)
    server.quit()



from_email = input("enter your email: ")
to_email = input("enter your friend email: ")
subject = input("enter subject: ")
mess = input("enter message: ")

send_email(from_email, to_email, subject, mess)