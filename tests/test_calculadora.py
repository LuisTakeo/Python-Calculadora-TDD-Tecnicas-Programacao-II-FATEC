import pytest

from calculadora.calculadora import Calculadora


def test_soma():
    calc = Calculadora()
    assert calc.soma(2, 3) == 5


# def test_subtrai():
#     calc = Calculadora()
#     assert calc.subtrai(5, 3) == 2


# def test_multiplica():
#     calc = Calculadora()
#     assert calc.multiplica(4, 3) == 12


# def test_divide():
#     calc = Calculadora()
#     assert calc.divide(10, 2) == 5


# def test_divide_por_zero():
#     calc = Calculadora()
#     with pytest.raises(ZeroDivisionError):
#         calc.divide(1, 0)
