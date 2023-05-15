import telnetlib
import base64



email = "pas2017@interia.pl"
password = "P4SInf2017"
pop3_server = "interia.pl"
pop3_port = 110

username = base64.b64encode(email.encode()).decode()
password = base64.b64encode(password.encode()).decode()

connection = telnetlib.Telnet(pop3_server, pop3_port)

response = connection.read_until(b"\n")
print(response.decode())

connection.write(b"USER " + email.encode() + b"\r\n")
response = connection.read_until(b"\n")
print(response.decode())

connection.write(b"PASS " + password.encode() + b"\r\n")
response = connection.read_until(b"\n")
print(response.decode())

connection.write(b"LIST\r\n")
response = connection.read_until(b"\n")
print(response.decode())

response_lines = response.decode().split("\n")[1:-2]
largest_mess_num = 0
largest_mess_size = 0

for line in response_lines:
    mess_num, mess_size = line.split()
    mess_num = int(mess_num)
    mess_size = int(mess_size)
    if mess_size > largest_mess_size:
        largest_mess_size = mess_size
        largest_mess_num = mess_num    
print(f"the largest mess {mess_num}, size {mess_size}")

connection.write(b"RETR " + str(largest_mess_num) + b"\r\n")
response = connection.read_until(b"\r\n")
print(f"largest messege content: {response.decode()}")

connection.write(b"QUIT\r\n")
response = connection.read_until(b"\n")
print(response.decode())
connection.close()