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
result, mailboxs = mail.list()

mes_count = 0

for mailbox in mailboxs:
    mailbox_name = mailbox.decode().split(' "/" ')[-1]
    response, local_mes_count = mail.select(mailbox_name,readonly=True)
    if response == "OK":
        mes_count += int(local_mes_count[0])

print(mes_count)












