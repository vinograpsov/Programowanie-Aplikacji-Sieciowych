import socket

HOST = '127.0.0.1'
PORT = 2900

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

print(f"You have connected to server {HOST}:{PORT}")

while True:
    number = input("Podaj liczbę: ")
    try:
        sock.sendall(number.encode())

        data = sock.recv(1024).decode()
        print(data)

        if data == "Odgadłeś liczbę!":
            sock.close()
            break
    except ValueError:
        print("Błąd! Wprowadzona wartość musi być liczbą!")

