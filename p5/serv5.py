import socket
import os
import sys
from datetime import datetime

bufferSize = 1024


def server(address, port):
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.bind((address, port))
    while True:
        client_message = s.recvfrom(bufferSize)
        message = client_message[0].decode("utf-8")
        client_address = client_message[1]
        if message != "request":
            s.sendto("error".encode("utf-8"), client_address)
            continue

        now = datetime.now()
        now_str = now.strftime("%H:%M:%S")
        s.sendto(now_str.encode("utf-8"), client_address)


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

    server(address, port)
