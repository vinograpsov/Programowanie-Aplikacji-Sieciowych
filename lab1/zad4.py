import ipaddress
import socket 


adress = input("ipadress: ")
try:
    tmp = socket.gethostbyaddr(adress)[0]
    print(tmp)
except Exception as ex:
    print(ex)