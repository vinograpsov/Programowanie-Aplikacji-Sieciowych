import ipaddress

adress = input("ipadress: ")
try:
    ipaddress.ip_address(adress)
    print("Poprawny")
except Exception as ex:
    print(ex)