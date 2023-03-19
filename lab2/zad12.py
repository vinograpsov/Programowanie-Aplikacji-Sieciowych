import socket

def recvall(sock, msgLen):
    msg = ""
    bytesRcvd = 0

    while bytesRcvd < msgLen:

        chunk = sock.recv(msgLen - bytesRcvd)

        if not chunk:
            break

        bytesRcvd += len(chunk)
        msg += chunk

    return msg


sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = '127.0.0.1'
server_port = 2908

try: 
    sockIPv4.connect((server_address, server_port))

    message = input("Enter message (up to 20 characters): ")
    message = message[:20].ljust(20) 
    sockIPv4.sendall(message.encode())

    mess = recvall(sockIPv4, 20)
    if mess:
        print("Received from server: {}".format(mess))
    else:
        print("Error receiving message from server")

except Exception as e:
    print(e)

sockIPv4.close()
