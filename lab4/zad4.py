import socket
import sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2902

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print ("[%s] UDP Calc Server is waiting for incoming connections ... " % strftime("%Y-%m-%d %H:%M:%S", gmtime()))

try:
    while True:

        data1, address = sock.recvfrom(4096)
        op, address = sock.recvfrom(4096)
        data2, address = sock.recvfrom(4096)

        data1 = data1.decode()
        data2 = data2.decode()
        op = op.decode()
        print(address)

        if data1 and data2 and op:

            op = str(op)

            print ("[%s] Got from client %s ... : %s %s %s" % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), str(address), data1, op, data2))

            try :

                if op == '+':
                    result = float(data1) + float(data2)
                elif op == '-':
                    result = float(data1) - float(data2)
                elif op == '*':
                    result = float(data1) * float(data2)
                elif op == '/':
                    result = float(data1) / float(data2)
                else:
                    result = "Bad operator. I support only +, -, *, / math operators"

                sock.sendto(str(result.encode), address)


            except ValueError as e:
                result = "%s" % e
                sent = sock.sendto(str(result).encode(), address)

            except:
                result = "Error"
                sent = sock.sendto(str(result).encode(), address)
finally:

    sock.close()
