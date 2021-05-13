import pytest
from unit_tests.models.integers.integers import Integers

pytestmark = pytest.mark.unit


class TestNumbers:
    def test_add_numbers(self):
        x = 1
        y = 1
        expected_value = x + y
        assert expected_value == Integers().add(x=x, y=y)

    def test_divide_numbers(self):
        x = 10
        y = 2
        expected_value = x / y
        assert expected_value == Integers().divide(x=x, y=y)

    def test_zero_division_error(self):
        x = 10
        y = 0
        with pytest.raises(ZeroDivisionError):
            Integers().divide(x=x, y=y)

