import socket

server_address = ('127.0.0.1', 2909)

datagram = "ed740b550024effd70726f6772616d6d696e6720696e20707974686f6e2069732066756e"

source_port = int(datagram[0:4], 16)
destination_port = int(datagram[4:8], 16)
length = int(datagram[8:12], 16)
checksum = int(datagram[12:16], 16)
data = bytes.fromhex(datagram[16:]).decode()

message = f"zad14odp;src;{source_port};dst;{destination_port};data;{data}"

print("source_port ",source_port)
print("destination_port ", destination_port)
print("length ",length)
print("checksum ",checksum)
print("data ", data)




sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1.0)
connected = sock.connect_ex(server_address)

if connected == 0:
    sock.send(message.encode())
    answer = sock.recv(1024).decode()
else:
    print("connection failed")

sock.close()
print("connection closed")



