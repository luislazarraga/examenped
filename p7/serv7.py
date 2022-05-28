import sys, os, socket, queue, time, datetime
import select
import noticia


noti = noticia.Noticia("Texto")
noticia2 = noticia.Noticia("Parrafada")
noticias = [noti, noticia2]

lista_usuarios = []

#Binding socket
def server(server_address, server_port):
    
    #Create Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Estableciendo conexión con {} en el puerto {}'.format(*server_address))
    sock.setblocking(0) #Paradigma no bloqueante
    #Binding the socket
    sock.bind((server_address, server_port))
    #Listening MAX 5 addresses at the same time
    sock.listen(5)
    
    inputs = [sock]
    outputs = []
    message_queues = {}
    print("Escuchando")

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        print(readable, exceptional)
    
        for elem in exceptional:
            inputs.remove(elem)
            if sock in outputs:
                outputs.remove(elem)
            sock.close()
            del message_queues[elem]

        for elem in readable:
            try:
                if elem is sock:
                    connection, client_address = sock.accept()
                    print("Conectado con:{}".format(client_address))
                    connection.setblocking(0)
                    inputs.append(connection)
                    message_queues[connection] = queue.Queue()
                else:
                    mensaje = elem.recv(4096).decode('utf8')
                    mensaje = mensaje.split()
                    print(mensaje)

                    if mensaje[0] == "nick":
                        if mensaje[1] in lista_usuarios:
                            elem.send(b"NACK")
                            print("Fallo en registrar cliente: {}".format(mensaje[1]))
                        else:
                            elem.send(b"ACK")
                            lista_usuarios.append(mensaje[1])

                    elif mensaje[0] == "request":
                        for aux in noticias:
                            #elem.send(aux.asunto.encode('utf8'))
                            elem.send(aux.texto.encode("utf-8"))
                            time.sleep(1)
                            elem.send(b"\nfin-de-mensaje\n")                     

                    elif mensaje[0] == "escribir":
                        #asunto = mensaje[1]
                        texto = mensaje[1:]
                        texto = "".join(texto)
                        aux = noticia.Noticia(texto)
                        noticias.append(aux)
                        elem.send(b"noticia-recibida")

            except IndexError:
                elem.close()
                print("cerro")
                inputs.remove(elem)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        address = '0.0.0.0'
        port = 65432
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Error en los argumentos")
        exit(1)

    server(address, port)
