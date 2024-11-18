import socket
import time
import logging
import unittest
logger = logging.getLogger(__name__)

class ChangeableList:
    def __init__(self, items=[]):
        # Initialize with a list of items or an empty list
        self.items = items
        self.ip = None
        self.port = None

    def set_host(self, HOST, PORT):
        self.ip = HOST
        self.port = PORT


    def add_item(self, item):
        """Add an item to the list."""
        self.items.append(item)

    def send_items(self):
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            #Connects to HOST, PORT
        while True:
            try:
                 c.connect((self.ip, self.port))
                 break
            except socket.error as e:
                logger.error("Not connected!")
                print(f"Connection failed: {e}. Reconnecting in 3 seconds...")
                time.sleep(1)
                print(f"Connection failed: {e}. Reconnecting in 2 seconds...")
                time.sleep(1)
                print(f"Connection failed: {e}. Reconnecting in 1 second...")
                time.sleep(1)

        while True:

            if self.items:
                c.send(str(self.items[0]).encode('utf8'))

                # Wait for acknowledgment from the server
                data = c.recv(1024)
                conf = data.decode('utf8')
                if conf == 'endtrip':
                    # Will print "End of queue!" when data is complete (server side)
                    print("End of queue!")
                    break
                else:
                    print("Server:", conf)

                # Pop the first element after receiving confirmation
                self.items.pop(0)

    # Ends the server connection
    def end_trip(self):
        self.add_item("endtrip")

class ClientTest(unittest.TestCase):
    def test_add_and_reset_items(self):
        obj = ChangeableList()
        obj.add_item(6)
        obj.add_item(4)
        obj.add_item(6)
        obj.add_item(8)
        obj.add_item("raid")

        # Check that items were added correctly
        self.assertEqual(obj.items, [6, 4, 6, 8, "raid"])

        obj.end_trip()

        # Check that the list was reset
        self.assertEqual(obj.items, [])

    def test_send_items(self):
        if not self.ip or not self.port:
            raise ValueError("IP address or port is not set")

        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            c.connect((self.ip, self.port))
            # Assuming you send items to the server here
            c.sendall(str(self.items).encode('utf-8'))  # Example of sending data
        finally:
            c.close()

    def test_send_items(self):
        obj = ChangeableList()
        obj.ip = "127.0.0.1"
        obj.port = 8080

        obj.add_item("test")

        # Mock the send operation for testing
        with unittest.mock.patch('socket.socket.connect') as mock_connect:
            with unittest.mock.patch('socket.socket.sendall') as mock_sendall:
                obj.send_items()
                mock_connect.assert_called_once_with(("127.0.0.1", 8080))
                mock_sendall.assert_called_once()

if __name__ == "__main__":
    unittest.main()