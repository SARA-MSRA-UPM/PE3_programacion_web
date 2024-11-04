# Practica Entregable 3 - Programación Web

Este repositorio contiene el código de la práctica entregable "Programación Web"
de la asignatura Software Avanzado Radar (SARA) del Master en Sistemas Radar.

El repositorio contiene las siguientes carpetas:
- `app`: contiene el archivo main.py para ejecutar la aplicación y la carpeta
  `src` donde se sitúan el resto de archivos.
- `app/src`: contiene cada uno de los paquetes de python que usaremos durante
  el desarrollo de la práctica dividido de forma básica por las diferentes
  funcionalidades.
  - `actors`: contiene las distintas clases con la lógica de funcionamiento
  principal de la práctica
  - `dataModels`: contiene clases con las distintas estructuras de datos que se
  utilizaran
  - `helpers`: contiene archivos con funcionalidades generales del proyecto
  que pueden ser utilizadas por cualquier clase principal.
  - `graphics`: contiene las clases utilizadas para la visualización de los
  distintos datos y objetos del escenario.

## Escenario de la práctica
El escenario de la práctica consiste en una implementación de un modelo
digital de un radar. Además del modelo del radar también existe un modelo
digital de puntos con distintas características que pueden ser detectados por
el radar. Esta práctica amplia las funcionalidades de la 
[Práctica Guiada 3](https://github.com/SARA-MSRA-UPM/PG3_programacion_web) y 
toma su escenario como base.


## Ejecución
El primer paso para realizar esta práctica es descargar el proyecto 
[RadarServer](https://github.com/SARA-MSRA-UPM/RadarServer) y arrancar el 
servidor allí desarrollado tal y como se indica en sus instrucciones. Esto es 
indispensable para el desarrollo de la práctica.

El segundo paso para poder ejecutar la práctica y comprobar su funcionamiento
será la creación de un entorno virtual propio del proyecto. En PyCharm es
posible crear un entorno virtual mediante la interfaz gráfica. En caso
necesario los comandos son los siguientes.
```
# Linux
# Crear
python3 -m venv venv
# Activar
source venv/bin/activate
# Desactivar
deactivate

# Windows
# Crear
python3 -m venv venv
# Activar
venv\Scripts\activate.bat
venv\Scripts\Activate.ps1
# Desactivar
deactivate
```

Una vez creado el entorno virtual es necesario instalar las dependencias
propias del proyecto. Las dependencias están definidas en el fichero
`requirements.txt`. En PyCharm se pueden instalar las dependencias mediante la
interfaz gráfica. En caso necesario los comandos son los siguientes.
```
pip install -r requirements.txt
```

Por último tras instalar las dependencias necesarias en nuestro entorno
virtual podemos arrancar el proceso principal de nuestro proyecto ejecutando
el fichero `app/main.py`.
```
python3 app/main.py
```

## Objetivos a realizar
1. **Visualización de los datos obtenidos**
