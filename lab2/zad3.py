import socket

sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serever_address = "212.182.24.27"
serever_port = 2900

try:
    sockIPv4.connect((serever_address, serever_port))  
    while True: 
        data = input("send to server: ")
        sockIPv4.sendall(data.encode())
        print("From server", sockIPv4.recv(4096).decode())
except Exception as e:
    print(e)


sockIPv4.close()
