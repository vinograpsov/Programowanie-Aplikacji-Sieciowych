import socket

import socket

sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = "127.0.0.1"
server_port = 2901

try: 
    while True:
        mess = input("what to send: ")
        sockIPv4.sendto(mess.encode(),(server_address, server_port))

        data, server = sockIPv4.recvfrom(4096)
        print("Server: ", data.decode())
except Exception as e:
    print(e)


sockIPv4.close()