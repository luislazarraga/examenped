import socket
import sys
from time import sleep
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
    rutafichero = "Hola.txt" 
    print('Enviando {}'.format(rutafichero))
    sock.sendall(rutafichero.encode('utf8'))
    

    amount_received = 0
    amount_expected = len(rutafichero)

    while amount_received < amount_expected:
        data = sock.recv(64)
        amount_received += len(data)
        print('Received {}'.format(data.decode('utf8')))

finally:
    print('Cerrando socket')
    sock.close()
