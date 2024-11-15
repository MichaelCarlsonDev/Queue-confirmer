import socket
import threading

def main_server(HOST, PORT):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()

    # Waits for a client to connect
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target = client_handle, args = (conn, addr))
        thread.start()
def set_host(self, HOST, PORT):
    self.ip = HOST
    self.port = PORT

def client_handle(conn, addr):

    # Runs the communication loop
    while True:
        data = conn.recv(1024)

        if not data:  # If no data is received, break the loop
            print('End of queue!')

        # Print the received data
        show = data.decode('utf8')
        print('Data:', show)

        # Send a confirmation to the client
        conn.send(str(1).encode('utf8'))

        # Identifies end of trip
        if show == "endtrip":
            conn.send(str(2).encode('utf8'))
            break



    # Handles clean closing of the client
    print("closed")
    conn.close()

if __name__ == "__main__":
    main_server()