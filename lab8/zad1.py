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

result, data = mail.uid('search', None, "ALL")
mail_ids = data[0]
id_list = mail_ids.split()
first_email_id = int(id_list[0])

result, data = mail.uid('fetch', bytes(str(first_email_id), 'utf-8'), 'BODY[HEADER.FIELDS (SUBJECT)]')
raw_email = data[0][1].decode('utf-8')  
mes = email.message_from_string(raw_email)
print(decode_header(mes['Subject'])[0])
mail.uid('STORE', bytes(str(first_email_id), 'utf-8'), '+FLAGS', '(\Seen)')















