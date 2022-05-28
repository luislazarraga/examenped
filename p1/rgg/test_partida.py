#!/usr/bin/env python3
import unittest

from partida import calcular_resultado

class PartidaTest(unittest.TestCase):

    def comprobar_partida(self, partida, esperado):
        calculado = calcular_resultado(partida)
        self.assertEqual(esperado, calculado, f"se esperaba {esperado} y ha salido {calculado}")

    def test_partida_0(self):
        partida = "00000000000000000000"
        esperado = 0
        self.comprobar_partida(partida, esperado)

    def test_partida_1(self):
        partida = "11111111111111111111"
        esperado = 20
        self.comprobar_partida(partida, esperado)

    def test_un_strike(self):
        partida = "X233500000000000000"
        esperado = 28
        self.comprobar_partida(partida, esperado)

    def test_3_strikes(self):
        partida = "XXX00000000000000"
        esperado = 60
        self.comprobar_partida(partida, esperado)

    def test_2_strikes(self):
        partida = "X8100000000X120001"
        esperado = 45
        self.comprobar_partida(partida, esperado)

    def test_1_spare(self):
        partida = "3/2100000000000000000"
        esperado = 15
        self.comprobar_partida(partida, esperado)


class PartidasTipicasTest(unittest.TestCase):
    Pcero =      (   0, "00000000000000000000" )
    Pperfecta =  ( 300, "XXXXXXXXXXXX" )
    Pnormal =    (  57, "11223344516070819000" )
    Pspare =     (  68, "1122334451607/819000" )
    Psparefin =  (  71, "1122334451607081904/4" )
    Pstrike =    (  72, "11223344X6271819000" )
    Pstrikefin = (  74, "112233445160708190X25" )

    def comprobar_partida(self, partida_con_resultado):
        esperado, partida = partida_con_resultado
        calculado = calcular_resultado(partida)
        self.assertEqual(esperado, calculado, f"se esperaba {esperado} y ha salido {calculado}")

    def test_calcular_resultado_Pcero(self):      self.comprobar_partida(self.Pcero)
    def test_calcular_resultado_Pnormal(self):    self.comprobar_partida(self.Pnormal)
    def test_calcular_resultado_Pspare(self):     self.comprobar_partida(self.Pspare)
    def test_calcular_resultado_Psparefin(self):  self.comprobar_partida(self.Psparefin)
    def test_calcular_resultado_Pstrike(self):    self.comprobar_partida(self.Pstrike)
    def test_calcular_resultado_Pstrikefin(self): self.comprobar_partida(self.Pstrikefin)
    def test_calcular_resultado_Pperfecta(self):  self.comprobar_partida(self.Pperfecta)


if __name__ == '__main__':
    unittest.main()
