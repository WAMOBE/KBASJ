# calculadora 
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b

import pytest
from Calculadora import Calculadora
def test_sumar():
 calc = Calculadora()
 assert calc.sumar(3, 5) == 8
 assert calc.sumar(-1, 1) == 0
def test_restar():
 calc = Calculadora()
 assert calc.restar(10, 5) == 5
def test_multiplicar():
 calc = Calculadora()
 assert calc.multiplicar(3, 4) == 12
def test_dividir():
 calc = Calculadora()
 assert calc.dividir(10, 2) == 5
 with pytest.raises(ValueError):
    calc.dividir(10, 0)



