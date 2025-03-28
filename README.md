# Servidor TCP para KOSMOS

Este proyecto es un servidor TCP simple desarrollado en Python para el proyecto KOSMOS.

## Autor

* Alexis Jesús Betancourt Silva
* Correo electrónico: [chonchah@gmail.com](mailto:chonchah@gmail.com)
* Github: [github.com/Chonchah](https://github.com/Chonchah)

## Descripción

Este servidor utiliza el protocolo TCP para establecer conexiones con clientes y recibir mensajes. El servidor convierte los mensajes a mayúsculas y los envía de vuelta al cliente.

## Uso

1. Clona el repositorio: `git clone https://github.com/chonchah/Kosmos-python-test.git` y has un **cd**
2. Ejecuta el servidor: `python server.py`
3. Conecta un cliente al servidor utilizando el comando ```bash python3 client.py```

## Instrucciones para ejecutar el servidor

### Paso 1: Clona el repositorio

Clona el repositorio utilizando el comando y has un **cd** dentro de este:
`git clone https://github.com/chonchah/Kosmos-python-test.git`
### Paso 2: Instala las dependencias

No cuenta con dependencias externas a las nativas incluidas en la instalacion de >python 3.11

### Paso 3: Ejecuta el servidor

Ejecuta el servidor utilizando el comando:
```bash python server.py ```
La salida debe lucir asi: 
```bash
$ python3 server.py 
Servidor iniciado en 127.0.0.1:5000
Conexión establecida con ('127.0.0.1', 62214)
```

### Paso 4: Conecta un cliente al servidor

Conecta un cliente al servidor utilizando el comando: ```bash python client.py ``` y envia un mensaje. La salida debe lucir asi:
```bash
$ python3 client.py 
Conectado al servidor en 127.0.0.1:5000
Mensaje: 
```

