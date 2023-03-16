import socket 

sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = "127.0.0.1"
server_port = 2902


try:
    sockIPv4.connect((server_address,server_port))

    sockIPv4.send("5".encode())
    sockIPv4.send("+".encode())
    sockIPv4.send("3".encode())

    data = sockIPv4.recv(4096)
    print(data.decode())



except Exception as e:
    print(e)