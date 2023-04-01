import socket
import time

HOST = '127.0.0.1'
PORT = 2900
NUM_PACKETS = 1000
MESSAGE = b"Hello, TCP!"

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect((HOST, PORT))

for _ in range(NUM_PACKETS):
    tcp_client.send(MESSAGE)

tcp_client.close()
