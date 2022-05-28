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
    inside = open(data, 'rb')
    stringy = inside.read()
    decodif = stringy.decode('utf8')

    print('Recibidos {} bytes desde {}'.format(len(data), address))
    print(decodif)

    if stringy:
        sent = sock.sendto(stringy, address)
        print('Sent {} bytes back to  {}'.format(sent, address))
