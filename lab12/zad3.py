import socket 
import random 

def start_server(address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((address, port))
        s.listen()
        print(f"Server is listening on {address}:{port}")


        while True:
            conn, addr = s.accept()
            with conn:
                print("Connected by", addr)
                num_rand = random.randint(1, 100)
                print(f"Random number: {num_rand}")     

                while True: 
                    data = conn.recv(1024)
                    if not data:
                        break

                    try:
                        guess = int(data)
                        if guess < num_rand:
                            conn.sendall(b"Too low")
                        elif guess > num_rand:
                            conn.sendall(b"Too high")
                        else: 
                            conn.sendall(b"You guessed it!")
                            break
                    except ValueError:
                        conn.sendall(b"Enter a number")


def main():
    address = "127.0.0.1"
    port = 8085

    try:
        start_server(address, port)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    