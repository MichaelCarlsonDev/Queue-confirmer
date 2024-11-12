import socket

HOST = '127.0.0.1'  # Localhost
PORT = 13200        # Same port as server

    # List of strings
q = ['read', 'bear', 'strike', 'alpha', 'slot', 4]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
    f.connect((HOST, PORT))

    while q:
    # Send the first element of the list
        f.sendall(str(q[0]).encode('utf8'))

    # Wait for acknowledgment from the server
        data = f.recv(1024)
        conf = data.decode('utf8')
        print("Server:", conf)

    # Pop the first element after receiving confirmation
        q.pop(0)

    # Will print "End of queue!" when data is complete (server side)