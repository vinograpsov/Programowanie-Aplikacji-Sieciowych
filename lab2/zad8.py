import socket 

server_address = input("ipaddress or hostname: ")

socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
timeout = 2 
socket_conn.settimeout(timeout)

#popular ports
port_list = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 443, 445, 465, 514, 587, 993, 995]

# port_list = [i for i in range(1,1001)]




open_ports = []
closed_ports = []
error_ports = []

for port in port_list:
    try:
        result = socket_conn.connect_ex((server_address,port))
        if result == 0:
            servive = socket.getservbyport(port)
            print("Port {} is open service: {}".format(port,servive))
            open_ports.append(port)
        else:
            servive = socket.getservbyport(port)
            print("Port {} is close service: {}".format(port,servive))
            closed_ports.append(port)
    except socket.error as ex:
        error_ports.append(port)
        print("Cant connect server on port {}".format(port))
        print("Blad {}".format(ex))


print("open ports: {}".format(open_ports))

print("closed ports: {}".format(closed_ports))

print("error ports: {}".format(error_ports))




# scanme.nmpa.org