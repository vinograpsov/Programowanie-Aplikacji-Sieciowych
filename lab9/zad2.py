import socket

address = 'httpbin.org'
port = 80
path = '/image/png'

def send_http_request(sock, address, path):
    request = f"GET {path} HTTP/1.1\r\nHost: {address}\r\n\r\n"
    sock.sendall(request.encode('utf-8'))

def receive_headers(sock):
    headers = b''
    while b'\r\n\r\n' not in headers:
        headers += sock.recv(1)
    return headers.decode('utf-8')


def receive_body(sock, content_length):
    body = b''
    while len(body) < content_length:
        body += sock.recv(1)
    return body


def main():
    with socket.create_connection((address, port)) as sock:
        send_http_request(sock, address, path)

        headers = receive_headers(sock).split('\r\n')
        content_length = 0

        for header in headers:
            if 'Content-Length' in header:
                content_length = int(header.split(': ')[1])

        image = receive_body(sock, content_length)

        with open("image.png", "wb") as file:
            file.write(image)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
