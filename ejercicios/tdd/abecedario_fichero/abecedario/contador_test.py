import unittest

from contador import Contador

class TestContadorLetras(unittest.TestCase):
    contador = Contador()

    def test_contador_devuelve_0(self):
        texto = "Hola prueba"
        letra = "m"
        resultado = self.contador.contarLetra(letra, texto)
        self.assertEqual(resultado, 0)

    def test_contador_devuelve_1(self):
        texto = "Hola prueba"
        letra = "o"
        resultado = self.contador.contarLetra(letra, texto)
        self.assertEqual(resultado, 1)

    def test_contador_devuelve_5(self):
        texto = "Hola prueba alas amor"
        letra = "a"
        resultado = self.contador.contarLetra(letra, texto)
        self.assertEqual(resultado, 5)

    def test_contador_de_string_2_letras_en_la_cadena_1_repeticion(self):
        texto = "Hola prueba"
        string = "pr"
        resultado = self.contador.contarString(string, texto)
        self.assertEqual(resultado, 1)

    def test_contador_de_string_2_letras_en_la_cadena_2_repeticiones(self):
        texto = "Hola prueba prima"
        cadena = "pr"
        resultado = self.contador.contarString(cadena, texto)
        self.assertEqual(resultado, 2)

    def test_contador_de_string_3_letras_en_la_cadena(self):
        texto = "Somos demasiado profesionales en la vida pro pues"
        cadena = "pro"
        resultado = self.contador.contarString(cadena, texto)
        self.assertEqual(resultado, 2)

    def test_contador_de_letras_mayusculas(self):
        texto = "Hola Mundo"
        cadena = "m"
        resultado = self.contador.contarLetra(cadena, texto)
        self.assertEqual(resultado, 1)

    def test_contador_de_letras_mayusculas(self):
        texto = "Hola Mundo"
        cadena = "O"
        resultado = self.contador.contarLetra(cadena, texto)
        self.assertEqual(resultado, 2)

    def test_contador_de_letras_mayusculas(self):
        texto = "Hola Mundo"
        cadena = "O"
        resultado = self.contador.contarLetra(cadena, texto)
        self.assertEqual(resultado, 2)

    def test_contador_busqueda_de_varias_letras(self):
        texto = "Hola prueba"
        arrayletras = ["a", "b", "r"]
        resultados = self.contador.contarVariasLetras(arrayletras, texto)
        self.assertEqual(resultados, [2, 1, 1])

    def test_contador_busqueda_de_4_letras(self):
        texto = "Hola prueba"
        arrayletras = ["a", "b", "r", "f"]
        resultados = self.contador.contarVariasLetras(arrayletras, texto)
        self.assertEqual(resultados, [2, 1, 1, 0])

    def test_encontrar_palindroma(self):
        texto = "No traces en ese cartón"
        



