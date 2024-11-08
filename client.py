import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define host and port (must match the server's)
    host = '127.0.0.1'  # Localhost
    port = 12345        # Same port as server

    # Connect to the server
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    # Send a message to the server
    message = "Hello from the client!"
    client_socket.send(message.encode('utf-8'))

    # Receive a response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {response}")

    # Close the connection
    client_socket.close()
    print("Connection closed")

if __name__ == "__main__":
    start_client()
