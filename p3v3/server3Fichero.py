import os, time, sys
nombre_fifo = '/tmp/envio'
nombre_fifo2 = '/tmp/vuelta'
def server():
    fifo_lectura = open(nombre_fifo, 'r')
    mensaje = fifo_lectura.read()
    print("Mensaje recibido")
    info = open(mensaje, 'r')
    data = info.read()

    fifo_escritura = os.open(nombre_fifo2, os.O_WRONLY)
    os.write(fifo_escritura, data.encode('utf8'))  
        






if __name__ == "__main__":
    if not os.path.exists(nombre_fifo):
        os.mkfifo(nombre_fifo)
    if not os.path.exists(nombre_fifo2):
        os.mkfifo(nombre_fifo2)

    server()
