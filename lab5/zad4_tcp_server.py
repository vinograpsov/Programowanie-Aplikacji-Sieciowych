import socket
import time

HOST = '127.0.0.1'
PORT = 2900
NUM_PACKETS = 1000

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind((HOST, PORT))
tcp_server.listen(1)

conn, addr = tcp_server.accept()

start_time = time.time()

for _ in range(NUM_PACKETS):
    data = conn.recv(1024)

end_time = time.time()

conn.close()
tcp_server.close()

print(f"TCP time: {end_time - start_time:.4f} seconds")
