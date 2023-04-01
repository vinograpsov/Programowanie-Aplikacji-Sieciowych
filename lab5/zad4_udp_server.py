import socket
import time

HOST = '127.0.0.1'
PORT = 2901
NUM_PACKETS = 1000

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind((HOST, PORT))

start_time = time.time()
for _ in range(NUM_PACKETS):
    data, addr = udp_server.recvfrom(1024)

end_time = time.time()
udp_server.close()

print(f"UDP time: {end_time - start_time:.4f} seconds")
