import socket

server_address = '127.0.0.1'
server_port = 2906

sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        sockIPv4.connect_ex((server_address,server_port))
        hostname = input("Hostname address: ")
        sockIPv4.send(hostname.encode())

        data = sockIPv4.recv(4096).decode()
        print(data)
except Exception as e:
    print(e)
