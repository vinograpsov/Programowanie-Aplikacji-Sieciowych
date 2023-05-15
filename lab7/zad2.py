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
total_size = sum(int(line.split()[1]) for line in response_lines)
print(f"{total_size} bites")

connection.write(b"QUIT\r\n")
response = connection.read_until(b"\n")
print(response.decode())
connection.close()