import socket

HOST = '127.0.0.1'  # Localhost
PORT = 13200        # Same port as server

class ChangeableList:
    def __init__(self, items=None):
        # Initialize with a list of items or an empty list
        self.items = []

    def add_item(self, item):
        """Add an item to the list."""
        self.items.append(item)

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
    print("End of queue!")
