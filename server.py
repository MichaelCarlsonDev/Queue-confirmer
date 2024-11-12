import socket

HOST = "127.0.0.1" #localhost
PORT = 13200       #port

    # Connects to client host, port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    # Runs this when connected
    conn, addr = s.accept()
    with conn:

    # Converts data to read, prints, sends 1 to confirm (can be changed)
        while True:
            data = conn.recv(1024)
            show = data.decode('utf8')
            print('Data:' , show)
            conn.send(str(1).encode('utf8'))

    # Prints "End of queue!" when complete
            if not data:
                print('End of queue!')
                break