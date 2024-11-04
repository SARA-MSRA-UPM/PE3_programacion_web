# external imports
from threading import Thread, Event
from socket import socket
from ast import literal_eval

# internal imports
from ..dataModels.detection_model import DetectionModel


class StreamReader(Thread):
    def __init__(self, url: str, port: int):
        super().__init__()

        self.url = url
        self.port = port
        self.socket_client = socket()

        self._stop_event = Event()

    def run(self):
        self.open_socket_connection()
        try:
            buffer = ""
            while not self._stop_event.is_set():
                message_raw = self.socket_client.recv(1024)
                if not message_raw:
                    break  # Terminar si se cierra la conexión

                buffer += message_raw.decode()

                while '\n' in buffer:
                    message, buffer = buffer.split('\n', 1)
                    radar_name, distance_to_radar, facing = literal_eval(message)
                    detection = DetectionModel(
                        radar_name=radar_name,
                        distance_to_radar=float(distance_to_radar),
                        relative_facing=float(facing)
                    )
                    print(detection.__dict__)

        finally:
            self.socket_client.close()
            print("Conexión cerrada")

    def stop(self):
        self._stop_event.set()

    def open_socket_connection(self):
        print("Intentando conectar")
        print(f"{self.url} / {self.port}")
        self.socket_client.connect((self.url, self.port))
        print("Conexión realizada con el servidor")
