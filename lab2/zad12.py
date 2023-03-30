import socket
import sys

def recvall(sock, msg_len):
    msg = ""
    bytes_rcvd = 0

    while bytes_rcvd < msg_len:
        chunk = sock.recv(min(msg_len - bytes_rcvd, 20))

        if not chunk:
            break

        bytes_rcvd += len(chunk)
        msg += chunk.decode()

    return msg

def sendall(sock, msg):
    msg_len = len(msg)
    bytes_sent = 0

    while bytes_sent < msg_len:
        chunk = msg[bytes_sent : bytes_sent + 20]
        sent = sock.send(chunk.encode())
        if not sent:
            break
        bytes_sent += sent

HOST = '127.0.0.1'
PORT = 2908

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))

    message = input("Enter message: ")

    sendall(sock, message)

    response = recvall(sock, len(message))
    print("Received from server: {}".format(response))

except Exception as e:
    print(e)

sock.close()
