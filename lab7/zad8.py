import poplib 

email = "pas2017@interia.pl"
password = "P4SInf2017"
pop3_server = "interia.pl"
pop3_port = 110

server = poplib.POP3(pop3_server, pop3_port)

server.user(email)
server.pass_(password)

mess_count, mailbox_size = server.stat()
for mess_num in range (1, mess_count + 1):
    mess_info = server.list(mess_num)
    mess_size = mess_info[1].split()[1]
    print(f"mess num {mess_num}, mess size {mess_size}")

server.quit()