import socket

sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serever_address = "212.182.24.27"
serever_port = "2900"

try: 
    sockIPv4.connect((server_address, server_port))
    sockIPv4.sendall("test")
    sockIPv4.get
except Exception as e:
    print(e)


sockIPv4.close()
sockIPv6.close()