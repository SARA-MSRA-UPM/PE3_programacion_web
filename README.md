# Practica Entregable 3 - Programación Web

Este repositorio contiene el código de la práctica entregable "Tiempo Real" de
la asignatura Software Avanzado Radar (SARA) del Master en Sistemas Radar.

El repositorio contiene las siguientes carpetas:

- `app`: contiene el archivo main.py para ejecutar la aplicación y ficheros
relacionados con el código de la aplicación.
- `app/src`: contiene cada uno de los paquetes de python que usaremos durante el
  desarrollo de la práctica dividido de forma básica por las diferentes
  funcionalidades.
  - `actors`: contiene las distintas clases con la lógica de funcionamiento
  principal de la práctica
  - `helpers`: contiene archivos con funcionalidades generales del proyecto que
  pueden ser utilizada por cualquier clase principal.
  - `models`: contine clases que actuan como modelos de datos del proyecto.
  - `monitors`: contiene las clases relacionadas con la implementación de los
  monitores de la práctica.

## Escenario de la práctica

El escenario de la práctica consiste en una implementación de un modelo
digital de un radar. Además del modelo del radar también existe un modelo
digital de puntos con distintas características que pueden ser detectados por
el radar. La esctructura de la práctica es la desarrollada en la
[Práctica Guiada 3](https://github.com/SARA-MSRA-UPM/PG3_programacion_web).

Además necesitaremos para la ejecución de nuetra práctica un servidor local que
simula el escenario de radares. Este servidor está desarrollado en el proyecto
[RadarServer](https://github.com/SARA-MSRA-UPM/RadarServer). Para el desarrollar
la práctica es necesario arrancar el servidor de `RadarServer` como se describe
más adelante.

## Ejecución

### Arranque del servidor Radar Server

El primer paso para realizar esta práctica es descargar el proyecto
[RadarServer](https://github.com/SARA-MSRA-UPM/RadarServer) y arrancar el
servidor allí desarrollado tal y como se indica en sus instrucciones. Esto es
indispensable para el desarrollo de la práctica.

### Ejecución de la práctica

El primer paso para poder ejecutar la práctica y comprobar su funcionamiento
será la creación de un entorno virtual propio del proyecto. Normalmente el IDE
al no encontrar un entorno virtual creado preguntará automáticamente si se desea
crearlo. En cualquier caso se pude crear utilizando los siguientes comandos:

- Linux

```shell
python3 -m venv .venv
source .venv/bin/activate
```

- Windows

```powershell
python3 -m venv venv
venv\Scripts\Activate.ps1
```

Una vez creado el entorno virtual es necesario instalar las dependencias propias
del proyecto. Las dependencias están definidas en el fichero `requirements.txt`.
Generalmente hay opciones para instalarlas de forma automática desde el IDE,
pero también se pueden instalar manualmente utilizando el siguiente comando:

```shell
pip install -r requirements.txt
```

Por último tras instalar las dependencias necesarias en nuestro entorno virtual
podemos arrancar el proceso principal de nuestro proyecto ejecutando el fichero
`app/main.py`.

```shell
python3 app/main.py
```

## Objetivos a realizar

1. **Implementar la obtención de radares** El primer objetivo de esta práctica
es implementar la funcionalidad de obtención de radares del escenario. Estos
serán los que nosotros hemos configurado en la petición inicial pero debemos
obtenerlos para poder comprobar que son los correctos, utilizarlos para
visualización o cualquier otro uso.
2. **Visualización de los datos obtenidos** El objetivo de esta práctica
entregable es implementar la funcionalidad de visualización de detecciones. Se
debe crear una ventana de visualización a partir de las detecciones recibidas
mediante la conexión por socket TCP al servidor `RadarServer`.
   - La visualización que se pide como objetivo es similar a la desarrollada en
   la [Práctica entregable 2](https://github.com/SARA-MSRA-UPM/PE2_tiempo_real),
   aunque no es necesaria la vista que representaba los radares.
3. **Validar la solución con todos los escenarios** Para la entrega de la
práctica, junto con el código se deberán entregar unas capturas de la
visualización de cada escenario y un texto con la configuración de radares
utilizada para conseguirlas.

> [!WARNING]
> Las figuras de los escenarios no tienen porque estar en la región en la
> que se trabajó en la práctica 2 ($x,y \in [0,200]$). Conviene
> colocar rádares por distintas zonas para encontrar las áreas por las que
> se mueven los puntos en cada escenario.
