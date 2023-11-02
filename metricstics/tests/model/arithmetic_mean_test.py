"""Test Module for calculations."""
from metricstics.src.model.calculation import ArithmeticMean

# pylint: disable=R0903
# Too few public methods (1/2) (too-few-public-methods)


class TestArithmeticMean:
    """Test Arithmetic Mean."""

    def test_calculate_empty(self):
        """Create empty data and check it."""
        result = {}
        mean = ArithmeticMean()
        data = set()
        mean.calculate(data, result)

        assert result[str(mean)] == 0

    def test_calculate_even(self):
        """Create even data and clear it."""
        result = {}
        mean = ArithmeticMean()
        data = {1, 2, 3, 4}
        mean.calculate(data, result)

        assert result[str(mean)] == 2.5

    def test_calculate_odd(self):
        """Create odd data and check it."""
        result = {}
        mean = ArithmeticMean()
        data = {1, 2, 3, 4, 5}
        mean.calculate(data, result)

        assert result[str(mean)] == 3
