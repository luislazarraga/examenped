import socket
import sys

from datetime import datetime
now = datetime.now()

#Crear el UDS socket del cliente
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

#Conectar el socket al puerto donde se está escuchando

print('Introducir dirección del socket: ')
server_address = input()
print('Conectándo a {}'.format(server_address))
try:
    sock.connect(server_address)
except socket.error as msg:
    print(msg)
    sys.exit(1)

try:
    #Enviar los datos
    mensaje = now.strftime('%Y %m %d, %H:%M:%S')
    print('Enviando {!r}'.format(mensaje))
    sock.sendall(mensaje.encode('utf8'))

    amount_received = 0
    amount_expected = len(mensaje)

    while amount_received < amount_expected:
        data = sock.recv(64)
        amount_received += len(data)
        print('Received {!r}'.format(data))

finally:
    print('Cerrando socket')
    sock.close()
