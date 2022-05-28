import socket, select, sys, queue, os

class Contador():
    def contarLetra(self, letra, texto):
        resultado = 0
        letra2 = letra.upper() #Para no distinguir entre mayusculas ni minusculas
        letra3 = letra.lower()
        for char in texto:
            if char == letra3 or char == letra2:
                resultado += 1 #Primera implemtación basta con return 0
        return resultado

    def contarString(self, cadena, texto):
        resultado = 0
        cadena2 = cadena.upper()
        cadena3 = cadena.lower()
        longitud_cadena = len(cadena)
        for i in range(len(texto)):
            encontrar= texto[i:i + longitud_cadena]
            if encontrar == cadena2 or encontrar == cadena3:
                resultado += 1
        return resultado

    def contarVariasLetras(self, arrayletras, texto):
        resultados = []

        for i in range(0,len(arrayletras)):
            resultado = 0
            char = arrayletras[i]
            for x in texto:
                if x == char:
                    resultado += 1 #Primera implemtación basta con return 0
            resultados.append(resultado)
            del resultado
        return resultados

def server(server_address, server_port):
    contador = Contador()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(0)
    s.bind((server_address, server_port))
    s.listen(5)
    inputs = [s]
    outputs = []
    message_queues = {}
    print("Escuchando...")

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        print(readable, exceptional)

        for elem in exceptional:
            inputs.remove(elem)
            if s in outputs:
                outputs.remove(elem)
            s.close()
            del message_queues[elem]

        for elem in readable:

            try:
                if elem is s:
                    connection, client_address = s.accept()
                    print('Connected by', client_address)
                    connection.setblocking(0)
                    inputs.append(connection)
                    message_queues[connection] = queue.Queue()

                else:
                    mensaje = elem.recv(4096).decode("utf-8")
                    mensaje = mensaje.split()
                    print(mensaje)

                    if mensaje[0] == "contar-letra":
                        letra = mensaje[1]
                        fichero = mensaje [2]
                        contenido = open(fichero)
                        lectura = contenido.read()
                        contador = Contador.contarLetra(contador, letra, lectura)
                        elem.send(str(contador).encode("utf-8"))

                    elif mensaje[0] == "contar-string":
                        cadena = mensaje[1]
                        fichero = mensaje[2]
                        contenido = open(fichero)
                        lectura = contenido.read()
                        contador = Contador.contarString(contador, cadena, lectura)
                        elem.send(str(contador).encode("utf-8"))

                    elif mensaje[0] == "contar-letras":
                        arrayletras = mensaje[1], mensaje[2], mensaje[3]
                        fichero = mensaje[4]
                        contenido = open(fichero)
                        lectura = contenido.read()
                        contador = Contador.contarVariasLetras(contador, arrayletras, lectura)
                        elem.send(str(contador).encode("utf-8"))
            
            except IndexError:
                elem.close()
                print("cerro")
                inputs.remove(elem)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        address = "0.0.0.0"
        port = 65432
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Error en los argumentos")
        exit(1)

    server(address, port)
