import os
import sys

def servidor():
    os.close(client_readfd)
    os.close(client_writefd)
    server_readf = os.fdopen(server_readfd, 'r')
    file_name = server_readf.read()
    server_readf.close()
    print("El servidor lee el archivo llamado: {}".format(file_name))
    
    target_file = open(file_name, 'r')
    data = target_file.read()
    target_file.close()
    server_writef = os.fdopen(server_writefd, 'w')
    server_writef.write(data)


def cliente():
    os.close(server_writefd)
    os.close(server_readfd)
    client_writef = os.fdopen(client_writefd, 'w')

    file_name = sys.argv[1]

    client_writef.write(file_name)
    client_writef.close()
    client_readf = os.fdopen(client_readfd, 'r')
    data = client_readf.read()
    print(data)

if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Error en los argumentos")
            exit(1)

        server_readfd, client_writefd = os.pipe()
        client_readfd, server_writefd = os.pipe()

        pid = os.fork()
        if pid:
            # padre
            servidor()

        else:
            # hijo
            cliente()
