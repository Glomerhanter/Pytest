import pytest
from app.calculator import Calculator


class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_addind_success(self):
        assert self.calc.adding(self, 2, 2) == 4

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_division_success(self):
        assert self.calc.division(self, 8, 4) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(self, 3, 6) == 18

    def teardown(self):
        print('Выполнение метода "Teardown"')