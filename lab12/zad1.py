import socket 

def start_server(address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((address, port))
        s.listen()
        print(f"Server is listening on {address}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(data.decode('utf-8'))
                    conn.sendall(data)  



def main():
    address = "127.0.0.1"
    port = 8085

    try:
        start_server(address, port)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    