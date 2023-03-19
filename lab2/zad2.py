import socket

sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = "127.0.0.1"
server_port = 2900

try: 
    sockIPv4.connect((server_address, server_port))
    sockIPv4.sendall("test".encode())
    print(sockIPv4.recv(4096).decode())
except Exception as e:
    print(e)

sockIPv4.close()
