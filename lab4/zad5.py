import socket, select, sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2906

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print ("[%s] UDP ECHO Server is waiting for incoming connections on port %s ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), PORT))

try:
    while True:

        data, address = sock.recvfrom(4096)
        data = data.decode()
        
        print ('[%s] Received %s bytes from client %s. Data: %s' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(data), address, data))

        if data:

            try :

                hostname = socket.gethostbyaddr(data)
                answer = f"Host name of ip {data} is {socket.gethostbyaddr(data)[0]}"
                
                sock.sendto(answer.encode(), address)
                print ('[%s] Sent back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), address))

            except socket.herror as e:
                sent = sock.sendto("Sorry, an error occurred in gethostbyaddr".encode(), address)
                print ('[%s] Sent %s bytes bytes back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))
finally:
    sock.close()
