import socket
import sys

#Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind the socket to the port
server_address = ('localhost', 10000)

print('Empezando en la dirección {} con el puerto {}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\Esperando a recibir mensajes')
    data, address = sock.recvfrom(4096)

    print('Recibidos {} bytes desde {}'.format(len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('Sent {} bytes back to  {}'.format(sent, address))
