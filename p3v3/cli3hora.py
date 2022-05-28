import os, time, sys
from datetime import datetime
from time import sleep

nombre_fifo = '/tmp/ped33aasexo'

def cliente():
    fifo_escritura = os.open(nombre_fifo, os.O_WRONLY)
    now = datetime.now()
    fechahora = now.strftime("%Y %m %d, %H:%M:%S")
    time.sleep(1)
    os.write(fifo_escritura, fechahora.encode('utf8'))

cliente()

 





