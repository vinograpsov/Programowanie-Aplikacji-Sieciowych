import poplib 
import email

email_adr = "pas2017@interia.pl"
password = "P4SInf2017"
pop3_server = "interia.pl"
pop3_port = 110

server = poplib.POP3(pop3_server, pop3_port)

server.user(email_adr)
server.pass_(password)

mess_count, _  = server.stat()

largest_mess_num = 0
largest_mess_size = 0

for mess_num in range (1, mess_count + 1):
    mess_info = server.list(mess_num)
    mess_size = mess_info[1].split()[1]
    if mess_size > largest_mess_size:
        largest_mess_num = mess_num
        largest_mess_size = mess_size

response, mess_lines, _ = server.retr(largest_mess_num)
mess_content = b"\r\n".join(mess_lines).decode()
mess = email.message_from_string(mess_content)

for part in mess.walk():
    if part.get_content_type() == "text/plain":
        print(part.get_payload(decode=True).decode())


server.quit()