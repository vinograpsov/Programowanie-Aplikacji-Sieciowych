import imaplib
import email
from email.header import decode_header

# Serwer 212.182.24.27, 
# port 143, 
# konto: pasinf2017@infumcs.eduz 
# hasłem P4SInf2017
# (webmail:https://212.182.24.27:443)

server = "212.182.24.27"
port = "143"
user = "pasinf2017@infumcs.eduz"
password = "P4SInf2017"
webmail = "https://212.182.24.27:443"



mail = imaplib.IMAP4_SSL(server)
mail.login(user, password)
mail.select("INBOX")

result, data = mail.search( None, "ALL")
mail_ids = data[0]
id_list = mail_ids.split()

if id_list:
    first_email_id = id_list[0]
    mail.store(first_email_id, '+FLAGS', '\DELETED')
    mail.expunge()
















