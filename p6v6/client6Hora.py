import socket
import sys
from datetime import datetime

now = datetime.now()

#Crear socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#COnectar el socket al puerto y host en el que se está escuchando
server_address = ('localhost', 10000)
print('Conectándose a l host {} en el puerto {}'.format(*server_address))
sock.connect(server_address)

try:

    #Enviar data
    mensaje = now.strftime('%Y %m %d, %H:%M:%S').encode('utf8')
    print('Enviando {!r}'.format(mensaje))
    sock.sendall(mensaje)

    #Busca la respuesta, chequeala
    amount_received = 0
    amount_expected = len(mensaje)

    while amount_received < amount_expected:
        data = sock.recv(64)
        data2 = data.decode('utf8')
        amount_received += len(data)
        print('Recibido {!r}'.format(data2))

finally:
    print('Cerrando socket...')
    sock.close()
