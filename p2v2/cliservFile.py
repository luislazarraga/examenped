import os, sys

rcli, wserver = os.pipe()
rserv, wcli = os.pipe()

pid = os.fork()

if pid: #padre
    os.close(rcli)
    os.close(wcli)
    fd1 = os.fdopen(rserv, 'r')
    fichero = fd1.read()
    fd1.close()
    print("El server va a leer el contenido de {}".format(fichero))
    
    ficheroAbierto = open(fichero, 'r')
    contenido = ficheroAbierto.read()
    ficheroAbierto.close()
    escrituraServer = os.fdopen(wserver, 'w')
    escrituraServer.write(contenido)

else:
    os.close(rserv)
    os.close(wserver)
    fd2 = os.fdopen(wcli, 'w')
    fichero = sys.argv[1]
    fd2.write(fichero)
    fd2.close()
    lecturaRespuesta = os.fdopen(rcli, 'r')
    leido = lecturaRespuesta.read()
    print(leido)
