"""Test Module for calculations."""
from metricstics.src.model.calculation import Calculation

# pylint: disable=R0903
# Too few public methods (1/2) (too-few-public-methods)


class TestCalculation:
    """Test Calculation."""

    def test_calculate_empty(self):
        """Create empty data and check it."""
        result = {}
        calc = Calculation()
        data = set()
        calc.calculate_arithmetic_mean(data, result)

        assert result["ArithmeticMean"] == 0

    def test_calculate(self):
        """Create even data and clear it."""
        result = {}
        calc = Calculation()
        data = {1, 2, 3, 4}
        calc.calculate_arithmetic_mean(data, result)

        assert result["ArithmeticMean"] == 2.5

    def test_calculate2(self):
        """Create odd data and check it."""
        result = {}
        calc = Calculation()
        data = {1, 2, 3, 4, 5}
        calc.calculate_arithmetic_mean(data, result)

        assert result["ArithmeticMean"] == 3
