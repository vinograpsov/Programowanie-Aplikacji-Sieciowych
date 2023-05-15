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
print(f"messages in inbox: {len(id_list)}")














