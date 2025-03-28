import socket

# Dirección y puerto del servidor
HOST, PORT = "127.0.0.1", 5000

# Crear socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
s.connect((HOST, PORT))
print(f"Conectado al servidor en {HOST}:{PORT}")

# Bucle para enviar mensages
while True:
    # Enviar mensaje solicitado
    try:
        msg=input("Mensaje: ")
    except KeyboardInterrupt as ex:
        print("Cancelado por el usuario.")
        s.sendall(b"DESCONEXION")
        break
        
    s.sendall(msg.encode('utf-8'))
    # Verifica si el mensaje es DESCONEXION
    if msg == 'DESCONEXION':
        break
    else:
        print("Esperando respuesta")
        response = ''
       
        data = s.recv(1024)
        response += data.decode('utf-8')

        print("Respuesta del servidor:",response, sep='\n')
s.close()
print("Bye bye!")

