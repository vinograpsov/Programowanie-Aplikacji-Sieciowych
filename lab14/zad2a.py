import socket 
import ssl 

def receive_all(sock):
    response = b''
    while True:
        data = sock.recv(4096)
        if not data:
            break
        response += data
    return response

address = 'httpbin.org'
port = 443
request = f'GET /html HTTP/1.1\r\nHost: {address}\r\n' \
          f'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A\r\n' \
          f'Connection: close\r\n\r\n'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with socket.create_connection((address, port)) as sock:
    with context.wrap_socket(sock, server_hostname=address) as ssock:
        ssock.send(request.encode())
        response = receive_all(ssock).decode()


start = response.find('<html')
html = response[start:]


with open('output2a.html', 'w') as f:
    f.write(html)
