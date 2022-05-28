import socket
import os
import sys

bufferSize = 1024


def client(server_address, port):
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.sendto("request".encode("utf-8"), (server_address, port))
    time = s.recv(bufferSize).decode("utf-8")
    print(time)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        address = "127.0.0.1"
        port = 65432
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = sys.argv[2]
    else:
        print("error en los argumentos")
        exit(1)

    client(address, port)
