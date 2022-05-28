import os, time, sys
nombre_fifo = '/tmp/envio'
nombre_fifo2 = '/tmp/vuelta'

def cliente():
    fifo_escritura = os.open(nombre_fifo, os.O_WRONLY)
    rutafichero = "Hola.txt"
    os.write(fifo_escritura, rutafichero.encode('utf8'))
    print("Se ha enviado el fichero: " + rutafichero)
    os.close(fifo_escritura)

    fifo_lectura = open(nombre_fifo2, 'r')
    leido = fifo_lectura.read()
    print(leido)







if __name__ == "__main__":
    cliente()
