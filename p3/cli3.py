from time import sleep
import os
import sys
fifo_path = "/tmp/ped5_p3_app1"

def cliente(path):
        fifo_escritura = open(fifo_path, "w")
        pid = str(os.getpid())
        request = pid + " " + path
        fifo_escritura.write(request)
        fifo_escritura.close()

        fifo_lectura_path = fifo_path + "_{}".format(pid)
        try:

                os.mkfifo(fifo_path + "_{}".format(pid))
        except FileExistsError:
            pass

        fifo_lectura = open(fifo_lectura_path, "rb")
        text = fifo_lectura.read()
        fifo_lectura.close()
        os.write(1, text)
        os.unlink(fifo_lectura_path)


if __name__ == "__main__":
        if len(sys.argv) != 2:
                print("Error en los arguments.")
                exit(1)
        cliente(sys.argv[1])
