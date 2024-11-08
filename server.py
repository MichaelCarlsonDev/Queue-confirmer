import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define host and port
    host = '127.0.0.1'  # Localhost
    port = 12345        # Port to listen on

    # Bind the socket to an address and port
    server_socket.bind((host, port))

    # Set the server to listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Receive data from the client
    data = conn.recv(1024).decode('utf-8')
    print(f"Received from client: {data}")

    # Send a response to the client
    response = "Hello from the server!"
    conn.send(response.encode('utf-8'))

    # Close the connection
    conn.close()
    print("Connection closed")

if __name__ == "__main__":
    start_server()
