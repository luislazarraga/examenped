import socket
import sys, os

print("Donde quieres crear el socket")
server_address = input()

#Verificar que el socket no se ha creado
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

#Crear el socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

#Bindear el socket
print('Empezando en {}'.format(server_address))
sock.bind(server_address)

#Esperar a escuchar conexiones
sock.listen(2)

while True:
    
    #Esperar la conexión
    print('Esperando la conexión')
    connection, client_address = sock.accept()
    direct = str(client_address)
    try:
        print('Conexión desde: {}'.format(direct))

        #Recibir los datos en pequeños trozos  y retransmitelos
        while True:
            data = connection.recv(64)
            print('Recibido {!r}'.format(data))
            if data:
                print('Sending data back to the client')
                connection.sendall(data)
            else:
                print('No data from: ' + client_address)
                break

    finally:
        #Limpiar la conexión
        connection.close()
                





