import socket

server_address = input("ipadress ar hostname: ")
server_port = int(input("port: "))


socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket_conn.connect((server_address, server_port))
    print("Connected with server: {}:{}".format(server_address,server_port))
except socket.error as ex:
    print("Cant connect with server: {}:{}".format(server_address,server_port))
    print("Error: {}".format(ex))
finally:
    socket_conn.close()