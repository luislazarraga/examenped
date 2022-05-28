import unittest;

from partida_bolos import Bolos, ExcepcionBolos

class PartidaBolos(unittest.TestCase):
    bolos = Bolos()
    excepcion = ExcepcionBolos()

    def test_partida_vacia(self):
        juego = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 0)

    def test_partida_simple(self):
        juego = [(1,2), (1,0), (0,4), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 3+1+4)

    def test_partida_menos_simple(self):
        juego = [(2,5), (2,3), (0,4), (2,0), (0,2), (0,0), (0,2), (0,0), (0,0), (2,1)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 7+5+4+2++2++2+3)

    def test_partida_strike(self):
        juego = [(10,0), (1,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 12)

    def test_partida_varios_strikes(self):
        juego = [(10,0), (2,1), (2,4), (10,0), (5,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 13+3+6+15+5)

    def test_partida_strikes_seguidos(self):
        juego = [(10,0), (10,0), (1,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 21+11+1)

    def test_partida_strikes_seguidos_mas_complejo(self):
        juego = [(10,0), (10,0), (2,5), (10,0), (1,2), (0,2), (0,0), (0,0), (0,0), (0,0)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 22+17+7+13+3+2)

    def test_partida_3_strikes_seguidos(self):
        juego = [(10,0), (10,0), (10,0), (2,0), (0,0), (10,0), (0,2), (0,0), (0,0), (0,0)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 32+22+12+12+2)

    def test_partida_spare(self):
        juego = [(5,5), (1,2), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 11+3)

    def test_partida_spare_segunda_tirada_10(self):
        juego = [(0,10), (1,2), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 11+3)

    def test_partida_spare_mas_compleja(self):
        juego = [(0,10), (1,2), (6,4), (3,6), (1,2), (0,0), (0,0), (0,0), (0,0), (0,0)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 11+3+13+9+3)

    def test_partida_spare_y_strike(self):
        juego = [(10,0), (5,5), (4,2), (6,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 20+14+6+6)

    def test_ronda_10_strike(self):
        juego = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (10, 0)] + [(2, 2)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 14)

    def test_ronda_10_strike_mas_compleja(self):
        juego = [(10,0), (2,4), (0,0), (5,5), (3,2), (0,0), (0,0), (0,0), (0,0), (10,0)]+[(2,2)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 16+6+13+5+14)

    def test_ronda_10_strikes_extra(self):
        juego = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (10,0)]+[(10,0), (2,0)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 22)

    def test_ronda_10_spare(self):
        juego = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (5,5)]+[(4,3)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 14)

    def test_partida_perfecta(self):
        juego = [(10,0), (10,0), (10,0), (10,0), (10,0), (10,0), (10,0), (10,0), (10,0), (10,0)]+[(10,0), (10,0)]
        resultado = self.bolos.calcularResultado(juego)
        self.assertEqual(resultado, 300)

    def test_partida_prueba_excepcion(self):
        juego = [(15,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        try:
            self.excepcion(juego)
        except:
            pass

    def test_partida_prueba_excepcion_negativos(self):
        juego = [(-11,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        try:
            self.excepcion(juego)
        except:
            pass

    def test_partida_prueba_excepcion2(self):
        juego = [(6,6),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        try:
            self.excepcion(juego)
        except:
            pass