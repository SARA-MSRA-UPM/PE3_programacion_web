import logging
import socket
import requests
from math import cos, sin, radians
import matplotlib.pyplot as plt
from threading import Thread, Lock

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%H:%M:%S')

# Enviar configuración inicial
data = []
for i in range(0, 360, 120):
    data.append({
        "name": f"r{i}",
        "position_x": 0,
        "position_y": 0,
        "detection_range": 500,
        "orientation_initial": i,
        "increment": 1
    })
requests.post("http://localhost:8000/scenarioConfiguration", json=data)

# Configurar cliente de socket 
socket_client = socket.socket()
logging.info("Intentando conectar")
socket_client.connect(('127.0.0.1', 10003))
logging.info("Conexión realizada con el servidor")

# Configuración de la gráfica
fig, axe_map = plt.subplots(figsize=(10, 10))
points = []
points_lock = Lock()  # Lock para sincronizar el acceso a los puntos

def radar_detection_to_point(detection):
    """Convertir la detección en coordenadas x, y"""
    name, distance, facing = detection
    point_angle = radians(float(facing)+int(name[2:-1]))
    return (
        0 + float(distance) * cos(point_angle),
        0 + float(distance) * sin(point_angle),
    )

def receive_data(socket_client):
    buffer = ""
    try:
        while True:
            message_raw = socket_client.recv(1024)
            if not message_raw:
                break  # Terminar si se cierra la conexión
            
            buffer += message_raw.decode()
            
            while '\n' in buffer:
                message, buffer = buffer.split('\n', 1)
                logging.info(f"Mensaje recibido: {message}")
                detection_data = message[1:-1].split(',')
                p = radar_detection_to_point(detection_data)
                
                # Agregar el punto a la lista de puntos
                with points_lock:
                    points.append(p)
    finally:
        socket_client.close()
        logging.info("Conexión cerrada")

# Iniciar el hilo para recibir datos del radar
t = Thread(target=receive_data, args=(socket_client,))
t.start()

# Bucle principal para actualizar la gráfica
while t.is_alive() or points:
    with points_lock:
        while points:
            p = points.pop(0)
            axe_map.plot(p[0], p[1], 'ro')

    plt.draw()
    plt.pause(0.01)  # Pausar brevemente para actualizar la gráfica

plt.show()
t.join()
