import socket
import sys

#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
server_address = ('localhost', 10000)
print('Estableciendo conexión con {} en el puerto {}'.format(*server_address))
sock.bind(server_address)

#Listen for incoming connections
sock.listen(1)

while True:
    #Esperar la conexión
    print('Esperando una conexión...')
    connection, client_address = sock.accept()
    try:
        print('Conexión desde:', client_address)
        #Recibir los datos en pequeños cachos y retransmitirlos
        while True:
            data = connection.recv(64)    
            print('Mensaje recibido: \n{}\n'.format(data))
            
            if data:
                print('Enviando los datos de vuelta al cliente')
                connection.sendall(data)
            else:
                print('No hay datos de parte del cliente: {}', client_address)
                break

    finally:
        #Limpiar la conexión
        connection.close()
            
