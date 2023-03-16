import socket

import socket

sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = "127.0.0.1"
server_port = 2902

try: 
    while True:
        first = input("number ")
        opierator = input("operator ")
        second = input("number ")
        

        # message = f"{first} {opierator} {second}"
        # sockIPv4.sendto(message.encode(),(server_address, server_port))
        sockIPv4.sendto(first.encode(),(server_address, server_port))
        sockIPv4.sendto(opierator.encode(),(server_address, server_port))
        sockIPv4.sendto(second.encode(),(server_address, server_port))

        data, server = sockIPv4.recvfrom(4096)
        print("Server: ", data.decode())
except Exception as e:
    print(e)


sockIPv4.close()