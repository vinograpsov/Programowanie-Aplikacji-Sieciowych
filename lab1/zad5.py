import ipaddress
import socket 


hostname = input("hostname: ")
try:
    tmp = socket.gethostbyname(hostname)
    print(tmp)
except Exception as ex:
    print(ex)