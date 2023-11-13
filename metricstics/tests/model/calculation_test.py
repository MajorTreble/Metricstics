"""Test Module for calculations."""
from metricstics.src.model.calculation import Calculation


class TestCalculation:
    """Test Calculation."""

    def test_calculate_empty(self):
        """Create empty data and check it."""
        result = {}
        calc = Calculation()
        data = []

        calc.calculate_minimum(data, result)
        calc.calculate_maximum(data, result)
        calc.calculate_mode(data, result)
        calc.calculate_median(data, result)
        calc.calculate_arithmetic_mean(data, result)
        calc.calculate_mean_absolute_deviation(data, result)
        calc.calculate_standard_deviation(data, result)

        assert len(result) == 7
        assert result["Minimum"] == "Undefined"
        assert result["Maximum"] == "Undefined"
        assert result["Mode"] == "Undefined"
        assert result["Median"] == "Undefined"
        assert result["ArithmeticMean"] == "Undefined"
        assert result["MeanAbsoluteDeviation"] == "Undefined"
        assert result["StandardDeviation"] == "Undefined"

    def test_calculate(self):
        """Create even data and clear it."""
        result = {}
        calc = Calculation()
        data = [1, 2, 3, 3, 4, 5]

        calc.calculate_minimum(data, result)
        calc.calculate_maximum(data, result)
        calc.calculate_mode(data, result)
        calc.calculate_median(data, result)
        calc.calculate_arithmetic_mean(data, result)
        calc.calculate_mean_absolute_deviation(data, result)
        calc.calculate_standard_deviation(data, result)

        assert len(result) == 7
        assert result["Minimum"] == 1
        assert result["Maximum"] == 5
        assert result["Mode"] == 3
        assert result["Median"] == 3
        assert result["ArithmeticMean"] == 3
        assert round(result["MeanAbsoluteDeviation"], 10) == 1.2909944487
        assert result["StandardDeviation"] == 1.0
