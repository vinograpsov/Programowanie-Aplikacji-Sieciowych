import socket 

server_address = ('127.0.0.1', 2911)

datagram = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1bc0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c180 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 0100 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 6772 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e".replace(" ","")

protocol_version = int(datagram[0:1], 16)
protocol_type = int(datagram[18:20], 16)
source_ip_not_sep = datagram[24:32]
sourse_ip_str = f"{int(source_ip_not_sep[0:2], 16)}.{int(source_ip_not_sep[2:4], 16)}.{int(source_ip_not_sep[4:6], 16)}.{int(source_ip_not_sep[6:8], 16)}"
destination_not_sep = datagram[32:40]
destination_ip_str = f"{int(destination_not_sep[0:2], 16)}.{int(destination_not_sep[2:4], 16)}.{int(destination_not_sep[4:6], 16)}.{int(destination_not_sep[6:8], 16)}"
message_1 = f"zad15odpA;ver;{protocol_version};srcip;{sourse_ip_str};dstip;{destination_ip_str};type;{protocol_type}"

print("protocol_version", protocol_version)
print("protocol_type", protocol_type)
print("sourse_ip_str", sourse_ip_str)
print("destination_ip_str", destination_ip_str)
print("message_1", message_1)
print("-----------------------")

source_port = int(datagram[40:44], 16)
destinatain_port = int(datagram[44:48], 16)
data = bytes.fromhex(datagram[104:]).decode()
message_2 = f"zad15odpB;srcport;{source_port};dstport;{destinatain_port};data;{data}"


print("source_port", source_port)
print("destinatain_port", destinatain_port)
print("data", data)
print("message_2", message_2)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1.0)
connected = sock.connect_ex(server_address)

if connected == 0:
    sock.send(message_1.encode())
    answer_1 = sock.recv(1024).decode()
    print("server recived: ", answer_1)
    if answer_1 == "TAK":
        sock.send(message_2.encode())
        answer_2 = sock.recv(1024).decode()
        print("server recived: ", answer_2)

else:
    print("connection failed")

sock.close()
print("connection closed")












