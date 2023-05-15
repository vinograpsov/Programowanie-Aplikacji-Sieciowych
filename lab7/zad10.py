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

for mess_num in range(1, mess_count + 1):
    print(f"mess num {mess_num}")
    response, mess_lines, _ = server.retr(mess_num)
    mess_content = b"\r\n".join(mess_lines).decode()
    mess = email.message_from_string(mess_content)

    for part in mess.walk():
        if part.get_content_type() == "test/plain": 
            print (part.get_payload(decode=True).decode())
    
    print("\n" + "=" * 40 + "\n") 


server.quit()