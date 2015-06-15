import unittest

__author__ = 'paulo'

class ExemploTest(unittest.TestCase):
    def test_soma(self):
        resultado = 1+2
        self.assertEqual(3, resultado)
