import socket
import threading

HOST = '127.0.0.1'  # localhost
PORT = 13200         # Port for server

<<<<<<< HEAD
def handle_client(conn, addr):
    """Handle communication with the connected client."""
    print(f"Connected by {addr}")

    try:
        while True:
            # Receive data from the client (e.g., Raspberry Pi)
            data = conn.recv(1024)
            if not data:
                break  # If no data, client closed connection

            print(f"Received from {addr}: {data.decode('utf8')}")
            conn.sendall(b"OK")  # Send acknowledgment

    except Exception as e:
        print(f"Error with client {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection with {addr} closed.")

# Set up the server socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        # Accept incoming client connection
        conn, addr = server_socket.accept()

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
=======
q = [5,2,6,9,3,4]


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
    f.connect((HOST, PORT))
    message = str(q[0]) + ' '
    f.sendall(str(message).encode('utf8'))
    data = f.recv(1024)
    conf = data.decode('utf8')
    if conf == '1':
        q.pop(0)
        message = str(q[0])
        f.sendall(str(message).encode('utf8'))
    #elif conf == '0':
        #break
>>>>>>> parent of f921c02 (Finished server/client send/recieve)
