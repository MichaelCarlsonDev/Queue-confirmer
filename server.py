import socket

HOST = "127.0.0.1"  # localhost
PORT = 13200         # port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    # Waits for a client to connect
    conn, addr = s.accept()
    with conn:

        # Runs the communication loop
        while True:
            data = conn.recv(1024)

            if not data:  # If no data is received, break the loop
                print('End of queue!')
                break

            # Print the received data
            show = data.decode('utf8')
            print('Data:', show)

            # Send a confirmation to the client
            conn.send(str(1).encode('utf8'))
