import socket
import os
import sys
bufferSize = 4096


def client(server_address, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_address, server_port))
    
    while True:
        string_opciones = "Opcion 1: Contar repeticiones de una letra en un texto\n" + "Opcion 2: Contar repeticiones de strings en un texto\n" + "Opcion 3: Contar repeticiones de varias letras en el texto\n" + "Opcion 4: Salir\n"
        opcion = input(string_opciones)

        if opcion == "1":
            letra = input("Introduce la letra que quieres contar: ")
            texto = input("Introduce el texto: ")
            string_enviar = "contar-letra " + letra + " " + texto
            s.sendto(string_enviar.encode("utf-8"), (server_address, port))
            contador = s.recv(bufferSize).decode("utf-8")
            print("Número de repeticiones de la letra en el texto: ", contador)
            

        elif opcion == "2":
            cadena = input("Introduce la cadena de caracteres que quieres contar: ")
            texto = input("Introduce el texto: ")
            string_enviar = "contar-string " + cadena + " " + texto
            s.sendto(string_enviar.encode("utf-8"), (server_address, port))
            contador = s.recv(bufferSize).decode("utf-8")
            print("Número de repeticiones de la cadena en el texto: ", contador)
            

        elif opcion == "3":
            arrayletras = input("Introduce las letras que quieras contar, separadas por un espacio: ")
            texto = input("Introduce el texto: ")
            string_enviar = "contar-letras " + arrayletras + " " + texto
            s.sendto(string_enviar.encode("utf-8"), (server_address, port))
            contador = s.recv(bufferSize).decode("utf-8")
            print("Número de repeticiones de las letras en el texto: ", contador)
    

        elif opcion == "4":
            s.close()
            exit(1)
    
        else:
            print("Error en la opcion elegida")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        address = "127.0.0.1"
        port = 65432
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Error en los argumentos")
        exit(1)

    client(address, port)
