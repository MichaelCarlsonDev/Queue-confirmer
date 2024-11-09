import socket

HOST = '127.0.0.1'  # Localhost
PORT = 13200        # Same port as server

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
