import os, time, sys

nombre_fifo = '/tmp/ped33aasexo'

def server():
    fifo_lectura = open(nombre_fifo, 'r')
    hora = fifo_lectura.readline()[:-1]
    print("La fecha y hora es:" + hora) 


if __name__ == '__main__':
    if not os.path.exists(nombre_fifo):
        os.mkfifo(nombre_fifo)
    else: pass
    
    server()
