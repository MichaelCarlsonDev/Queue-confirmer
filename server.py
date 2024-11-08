import socket

def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 12345

    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024).decode('utf-8')
    print(f"Received from client: {data}")

    response = "Hello from the server!"
    conn.send(response.encode('utf-8'))

    conn.close()
    print("Connection closed")

if __name__ == "__main__":
    start_server()
