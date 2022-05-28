import sys, os, time
from datetime import datetime

rcli, wserv = os.pipe()
now = datetime.now()
date_time = now.strftime("Año: %Y, Mes: %m Día: %d. Son las  %H:%M:%S")
pid = os.fork()

if pid:
    os.close(rcli)
    fd1 = os.fdopen(wserv, 'w')
    fd1.write(date_time)

else:
    os.close(wserv)
    fd2 = os.fdopen(rcli, 'r')
    fechaHora = fd2.read()
    print(fechaHora)

