import socket
from queue import Queue

HOST = '127.0.0.1'  # Localhost
PORT = 13200        # Same port as server

q = Queue()
q.put(123)
q.put(234)
q.put(726)
q.put(9989)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
    f.connect((HOST, PORT))
    while not q.empty():
        message = str(q.get(0)) + ' '
        f.sendall(str(message).encode('utf8'))