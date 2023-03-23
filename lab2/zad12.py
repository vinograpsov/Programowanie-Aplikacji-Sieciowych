import socket
import sys

def recvall(sock, msg_len):
    msg = ""
    bytes_rcvd = 0

    while bytes_rcvd < msg_len:
        chunk = sock.recv(msg_len - bytes_rcvd)

        if not chunk:
            break

        bytes_rcvd += len(chunk)
        msg += chunk.decode()

    return msg

HOST = '127.0.0.1'
PORT = 2908
MAX_PACKET_LENGTH = 20

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))

    message = input("Enter message (up to 20 characters): ")
    # message = message[:20].ljust(20)

    sock.sendall(message.encode())

    response = recvall(sock, MAX_PACKET_LENGTH)
    print("Received from server: {}".format(response))

except Exception as e:
    print(e)

sock.close()
