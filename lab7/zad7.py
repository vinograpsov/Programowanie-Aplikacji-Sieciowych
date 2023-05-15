import poplib 

email = "pas2017@interia.pl"
password = "P4SInf2017"
pop3_server = "interia.pl"
pop3_port = 110

server = poplib.POP3(pop3_server, pop3_port)

server.user(email)
server.pass_(password)

mess_num, mailbox_size = server.stat()
print(f"mess count {mess_num}, mailbox size {mailbox_size}")

server.quit()