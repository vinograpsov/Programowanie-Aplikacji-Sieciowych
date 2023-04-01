import random
import socket
import select
import sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2900

number = random.randint(1, 10)

connected_clients_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connected_clients_sockets.append(server_socket)

print("[%s] TCP Random Server is waiting for incoming connections on port %s ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), PORT))

game_over = False

while not game_over:

    read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])

    for sock in read_sockets:

        if sock == server_socket:

            sockfd, client_address = server_socket.accept()
            connected_clients_sockets.append(sockfd)

            print("[%s] Client %s connected ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address))

        else:
            try:
                data = sock.recv(1024).decode()
                try:
                    guess = int(data)
                    if guess < number:
                        message = "Za mało!"
                        sock.sendall(message.encode())
                    elif guess > number:
                        message = "Za dużo!"
                        sock.sendall(message.encode())
                    else:
                        message = "Odgadłeś liczbę!"
                        sock.sendall(message.encode())
                        game_over = True
                        break
                except ValueError:
                    message = "Błędna wartość! Wysłana wartość musi być liczbą!"

            except:
                print("[%s]" % (strftime("%Y-%m-%d %H:%M:%S", gmtime())))
                sock.close()
                connected_clients_sockets.remove(sock)
                break

for sock in connected_clients_sockets:
    sock.close()
