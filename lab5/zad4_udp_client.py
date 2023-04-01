import socket
import time

HOST = '127.0.0.1'
PORT = 2901
NUM_PACKETS = 1000
MESSAGE = b"Hello, UDP!"

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for _ in range(NUM_PACKETS):
    udp_client.sendto(MESSAGE, (HOST, PORT))

udp_client.close()
