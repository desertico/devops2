"""

Unit test for the calculator library

"""


class TestCalculator:

    def test_addition(self):
        assert 4 == add(2, 2)

    def test_addition2(self):

        assert 5 == add(2, 3)

    def test_divide(self):

        assert 3 == add(4, 2)

    def test_substraction(self):

        assert 2 == subtract(4, 2)

    def test_multiplication(self):

        assert 100 == multiply(10, 10)

