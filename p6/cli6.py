import socket
import os
import sys
bufferSize = 4096


def client(server_address, server_port, file_name):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_address, server_port))
    s.sendto(file_name.encode("utf-8"), (server_address, port))

    while True:
        data = s.recv(bufferSize)
        if data == "fin_de_fichero":
            break
        os.write(1, data)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        address = "127.0.0.1"
        port = 65432
        file = sys.argv[1]
    elif len(sys.argv) == 4:
        address = sys.argv[1]
        port = int(sys.argv[2])
        file = sys.argv[3]
    else:
        print("Error en los argumentos")
        exit(1)

    client(address, port, file)
