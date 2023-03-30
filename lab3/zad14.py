import socket 

server_address = ('127.0.0.1', 2910)

datagram = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 1800 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee00 1a 4c ee 68 65 6c 6c 6f 20 3a 29".replace(" ","")

source_port = int(datagram[0:4], 16)
destination_port = int(datagram[4:8], 16)
data = bytes.fromhex(datagram[64:]).decode()

message = f"zad14odp;src;{source_port};dst;{destination_port};data;{data}"

print("source_port ",source_port)
print("destination_port ", destination_port)
print("data ", data)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1.0)
connected = sock.connect_ex(server_address)

if connected == 0:
    sock.send(message.encode())
    answer = sock.recv(1024).decode()
    print("server recived: ", answer)
else:
    print("connection failed")

sock.close()
print("connection closed")












