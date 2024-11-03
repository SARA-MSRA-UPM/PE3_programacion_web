import threading
import socket
from .socket_lector import SocketLector
from .radar_collection import RadarCollection

class SocketListener(threading.Thread):
    def __init__(self, port: int, file_path: str, radar_collection: RadarCollection):
        super().__init__()
        self.port = port
        self.file_path = file_path
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.radar_collection = radar_collection
        try:
            self.sock.bind(('127.0.0.1', self.port))
            self.sock.listen(0)
        except socket.error as e:
            self.sock.close()
            raise e
        

    def run(self):
        try:
            while True:
                connection, _ = self.sock.accept()
                lector = SocketLector(self.file_path, connection, self.radar_collection)
                lector.daemon = True
                lector.start()
        finally:
            self.sock.close()
    
    def stop(self):
        self.sock.close()