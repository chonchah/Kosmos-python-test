# TEST PYTHON & TCP PARA KOSMOS
# AUTOR: ALEXIS JESUS BETANCOURT SILVA
# EMAIL: chonchah@gmail.com
# Github: github.com/Chonchah

import socket
import sys

HOST, PORT = "127.0.0.1", 5000
class Server:
    def __init__(self):
        # Inicializa el servidor con la dirección y puerto dados
        self.host = HOST
        self.port = PORT
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start(self):
        print(f"Servidor iniciado en {self.host}:{self.port}")
        # Asigna la dirección y puerto al socket
        self.server.bind((self.host, self.port))
        # Se pone a la espera de conexiones
        self.server.listen()
        while True:
            client_socket, client_address = self.server.accept()
            print(f"Conexión establecida con {client_address}")
            # Maneja la conexión con el cliente
            exit = self.handle_client(client_socket)
            

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024)
            # Imprime el mensaje del cliente
            print("Mensaje del cliente:",data.decode('utf-8'), sep='\n')
            if data.decode('utf-8') == 'DESCONEXION':
                break     
            # Convierte el mensaje a mayúsculas y se lo envia al cliente
            response = data.decode('utf-8').upper()
            client_socket.sendall(response.encode('utf-8'))
        # Cerrar la conexión
        client_socket.close()
        print("Conexión cerrada, esperando nueva conexión...")

if __name__ == '__main__':
    server = Server()
    server.start()
    
