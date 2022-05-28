import socket
import os
import sys


def cliente(server_address, fichero):
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.connect(server_address)

    try:
        mensaje = fichero
        print('Dirección de fichero: {!r}'.format(mensaje))
        s.sendall(mensaje.encode('utf8'))

        while True:
            data = s.recv(1024)
            if not data:
                break

            os.write(1, data)

    finally:
        print("Cerrando socket...")
        s.close()


if __name__ == "__main__":

    if len(sys.argv) == 2:
        address = "/tmp/ped5_p4"
        file = sys.argv[1]
    elif len(sys.argv) == 3:
        address = "/tmp/" + sys.argv[1]
        file = sys.argv[2]
    else:
        print("Error en los argumentos")
        exit(1)

    cliente(address, file)
