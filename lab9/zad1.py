import socket

address = 'httpbin.org'
port = 80

def send_http_request(sock, address):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Safari/7.0.3"
    request = f"GET /html HTTP/1.1\r\nHost: {address}\r\nUser-Agent: {user_agent}\r\n\r\n"
    sock.sendall(request.encode('utf-8'))


def get_headers(sock):
    headers = ''
    while True:
        headers += sock.recv(1).decode('utf-8')
        if '\r\n\r\n' in headers:
            break
    return headers.split('\r\n')


def get_content_length(headers):
    for header in headers:
        if 'Content-Length' in header:
            return int(header.split(': ')[1])
    return None


def receive_data(sock, content_length):
    data = b''
    buf_size = 4096
    while content_length is None or len(data) < content_length:
        data += sock.recv(buf_size)
    return data.decode('utf-8')

def main():

    with socket.create_connection((address, port)) as sock:
        send_http_request(sock, address)

        headers = get_headers(sock)
        content_length = get_content_length(headers)

        html = receive_data(sock, content_length)

        with open("page.html", "w") as file:
            file.write(html)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")