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

result, data = mail.search( None, "(UNSEEN)")
mail_ids = data[0]
id_list = mail_ids.split()

for num in id_list:
    result, data = mail.fetch(num, 'BODY[TEXT]')
    raw_email = data[0][1].decode('utf-8')
    mes = email.message_from_string(raw_email)
    if mes.is_multipart():
        for payload in mes.get_payload():
            print(payload.get_payload())
    else:
        print(mes.get_payload())

    mail.store(num, '+FLAGS', '\Seen')















