import socket

def send_data_to_server(address, port, data):
    with socket.create_connection((address, port)) as sock:
        sock.sendall(data.encode())
        response = sock.recv(1024)
        print(f"Received: {response.decode()}")

def main():
    address = "127.0.0.1"
    port = 8085
    data = "Hello, server!"

    send_data_to_server(address, port, data)

if __name__ == "__main__":
    main()
