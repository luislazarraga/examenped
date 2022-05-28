import os, sys, socket

def cliente(server_address, server_port):
    #Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Conectándose a l host {} en el puerto {}'.format(server_address, server_port))
    sock.connect((server_address, server_port))
    print("Conxión establecida con {} en el puertp {}".format(server_address, server_port))
    print("Añada su nombre de usuario")
    
    nick_check = 0
    while True:
        if nick_check == 0:
            nick = input("Introduce tu Nickname: ")
            mensaje_nick = "nick " + nick
            sock.sendto(mensaje_nick.encode("utf-8"), (server_address, port))
            confirmacion = sock.recv(4096).decode("utf-8")
            if confirmacion == "ACK":
                print("Login exitoso")
                nick_check = 1
            else:
                print("Error en login")
                break

        menu = "\nOpción 1: Leer Noticias Existente \n"+ "Opción 2: Enviar noticia\n" + "Opción 3: Desconectar\n" + "Inserta:  "
        opciones = input(menu)

        if opciones == '1':
            #Leer
            enviarOpcion = "request"
            sock.sendto(enviarOpcion.encode('utf8'), (server_address, server_port))
            while True:
                noticias = sock.recv(4096).decode("utf-8")
                print(noticias)
                if noticias.strip() == "fin-de-mensaje":
                    break

        #Cliente recibiría
        elif opciones == '2':
            #Escribir
            noticiaAEnviar = input("Introduce la noticia:")
            new  = 'escribir ' + noticiaAEnviar
            sock.sendto(new.encode('utf8'), (server_address, server_port))
            confirmation = sock.recv(4096).decode('utf8')    
             
            if confirmation == "noticia-recibida":
                print("Noticia enviada exitosamente")
            else:
                print("Error al enviar")

        elif opciones == '3': 
            #Desconectar
            print("Cerrando conexión con el servidor")
            sock.close()
            exit(0)

        else:
            print("Input error, [1-3] only")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        address = '127.0.0.1'
        port = 65432
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Error en los argumentos")
        exit(1)
        
    cliente(address, port)
