import socket
import sys
from datetime import datetime

now = datetime.now()
#Create an UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)

message = now.strftime("%Y %m %d,  %H:%M:%S")

try:

    #Enviar la data
    print('Enviando {!r}'.format(message))
    sent = sock.sendto(message.encode('utf8'), server_address)

    #Recepción de la respuesta
    print('Esperando para recibir')
    data, server = sock.recvfrom(4096)
    print('Recibidos {!r}'.format(data))

finally:
    print('Cerrando socket')
    sock.close()
