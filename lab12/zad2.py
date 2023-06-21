import socket 
import datetime 

def log_event(event_message):
    with open("server_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} : {event_message}\n")


def start_server(address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((address, port))
        s.listen()
        log_event(f"Server is listening on {address}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                log_event(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
                    log_event(f"Received data: {data.decode('utf-8')}")  



def main():
    address = "127.0.0.1"
    port = 8085

    try:
        start_server(address, port)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    