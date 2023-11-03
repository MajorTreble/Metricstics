"""Test Module for controllers."""
from metricstics.src.controller.input_controller import InputController

# pylint: disable=R0903
# Too few public methods (1/2) (too-few-public-methods)


class TestInputController:
    """Test Input Controller."""

    def test_generate_random_data(self):
        """Create random data and check it."""
        controller = InputController()
        controller.generate_random_data(5)

        assert len(controller.data) == 5

    def test_clear_data(self):
        """Create random data and clear it."""
        controller = InputController()
        controller.generate_random_data(5)
        controller.clear_data()

        assert len(controller.data) == 0

    def test_calculate_arithmetic_mean(self):
        """Create random data and check it."""
        controller = InputController()
        controller.generate_random_data(5)
        result = controller.calculate_arithmetic_mean()

        assert len(result) == 1
        assert result["ArithmeticMean"] == 3

    def test_calculate_mean_absolute_deviation(self):
        """Create random data and check it."""
        controller = InputController()
        controller.generate_random_data(5)
        result = controller.calculate_mean_absolute_deviation()

        assert len(result) == 2
        assert result["MeanAbsoluteDeviation"] == 1.4142135623730951

    def test_calculate_standard_deviation(self):
        """Create random data and check it."""
        controller = InputController()
        controller.generate_random_data(5)
        result = controller.calculate_standard_deviation()

        assert len(result) == 2
        assert result["StandardDeviation"] == 1.2

    def test___str__(self):
        """Create random data and check it."""
        controller = InputController()
        controller.generate_random_data(5)
        string = str(controller)

        assert string == "{1, 2, 3, 4, 5}"
