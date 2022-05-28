import unittest

from area_triangulo import Triangulo


class TestAreaTriangulo(unittest.TestCase):

    def test_area_0(self):
        triangulo = Triangulo(0)
        self.assertEqual(triangulo.area, 0)

    def test_area_10(self):
        triangulo = Triangulo(0)
        triangulo.CalcularArea(10, 0)
        self.assertEqual(triangulo.area, 0)

    def test_area_25(self):
        triangulo = Triangulo(0)
        triangulo.CalcularArea(25, 2)
        self.assertEqual(triangulo.area, 25)

    def test_area_50(self):
        triangulo = Triangulo(0)
        triangulo.CalcularArea(10, 10)
        self.assertEqual(triangulo.area, 50)

    def test_area_80(self):
        triangulo = Triangulo(0)
        triangulo.CalcularArea(16, 10)
        self.assertEqual(triangulo.area, 80)



