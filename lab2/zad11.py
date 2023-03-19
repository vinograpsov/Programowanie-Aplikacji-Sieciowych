import socket

sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = '127.0.0.1'
server_port = 2908

try: 
    sockIPv4.connect((server_address, server_port))

    message = input("Enter message (up to 20 characters): ")
    message = message[:20].ljust(20) 
    
    sockIPv4.sendall(message.encode())

    response = sockIPv4.recv(20).decode()
    print("Received from: {}".format(response))

except Exception as e:
    print(e)

sockIPv4.close()
