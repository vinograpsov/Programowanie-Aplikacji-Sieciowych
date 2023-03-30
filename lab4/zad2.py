import socket, select
from time import gmtime, strftime

HOST = "127.0.0.1"
PORT = 2900

sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockIPv4.bind((HOST, PORT))
sockIPv4.listen(10)
print ("[%s] TCP ECHO Server is waiting for incoming connections on port %s ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), PORT))


while True:
    client, client_address = sockIPv4.accept()
    print ("[%s] Client %s connected ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address))



    while True:
        data = client.recv(4096)

        if not data:
            break

        print("Client send ", data.decode())
        server_answer = "Answer from server: " + str(data.decode())
    
        client.send(server_answer.encode())

client.close()
