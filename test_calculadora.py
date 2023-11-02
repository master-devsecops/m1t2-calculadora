import unittest
from calculadora import suma, resta, multiplicacion, division

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(5, 3), 8)
        self.assertEqual(suma(-2, 2), 0)
        self.assertEqual(suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(2, 5), -3)
        self.assertEqual(resta(0, 0), 0)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(5, 3), 15)
        self.assertEqual(multiplicacion(-2, 2), -4)
        self.assertEqual(multiplicacion(0, 5), 0)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(5, 2), 2.5)
        self.assertEqual(division(10, 0), "No es posible dividir entre cero")

if __name__ == '__main__':
    unittest.main()