import socket

HOST = "127.0.0.1" #localhost
PORT = 13200       #port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
    f.bind((HOST, PORT))
    f.listen()
    conn, addr = f.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            print('Data recieved!')
            show = data.decode('utf8')
            print(show)
            conn.send(str(1).encode('utf8'))
            if not data:
                print('End of queue!')
                #conn.send(str(0).encode('utf8'))
                break