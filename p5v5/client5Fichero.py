import socket
import sys

#Create an UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)

try:

    #Enviar la data
    rutafichero = "Hola.txt"
    print('Enviando {!r}'.format(rutafichero))
    sent = sock.sendto(rutafichero.encode('utf8'), server_address)

    #Recepción de la respuesta
    print('Esperando para recibir')
    data, server = sock.recvfrom(4096)
    data2 = data.decode('utf8')
    print('El fichero contiene: \n {}'.format(data2))

finally:
    print('Cerrando socket')
    sock.close()
