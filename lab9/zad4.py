import socket

address = 'httpbin.org'
port = 80
path = '/post'
user_data = {'field1': 'value1', 'field2': 'value2'}

def prepare_http_request(address, path, data):
    data = '&'.join(f"{key}={value}" for key, value in data.items())
    return f"POST {path} HTTP/1.1\r\nHost: {address}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(data)}\r\n\r\n{data}"

def send_http_request(sock, request):
    sock.sendall(request.encode('utf-8'))

def receive_data(sock, buffer_size = 4096):
    data = b''
    while True:
        part = sock.recv(buffer_size)
        data += part
        if len(part) < buffer_size:
            break
    return data

def main():
    with socket.create_connection((address, port)) as sock:
        
        request = prepare_http_request(address, path, user_data)
        send_http_request(sock, request)
        
        data = receive_data(sock)
        headers, body = data.split(b'\r\n\r\n', 1)


        print(body.decode('utf-8'))

        with open('response.txt', 'w') as file:
            file.write(body.decode('utf-8'))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")