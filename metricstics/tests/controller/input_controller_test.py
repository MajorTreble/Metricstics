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

    def test_calculate_minimum(self, mocker):
        """Create random data and check it."""
        controller = InputController()
        mocker.patch.object(controller, "data", new=[1, 2, 3, 3, 4, 5])
        controller.calculate_minimum()

        result = controller.get_result()
        assert len(result) == 1
        assert result["Minimum"] == 1

    def test_calculate_maximum(self, mocker):
        """Create random data and check it."""
        controller = InputController()
        mocker.patch.object(controller, "data", new=[1, 2, 3, 3, 4, 5])
        controller.calculate_maximum()

        result = controller.get_result()
        assert len(result) == 1
        assert result["Maximum"] == 5

    def test_calculate_mode(self, mocker):
        """Create random data and check it."""
        controller = InputController()
        mocker.patch.object(controller, "data", new=[1, 2, 3, 3, 4, 5])
        controller.calculate_mode()

        result = controller.get_result()
        assert len(result) == 1
        assert result["Mode"] == 3

    def test_calculate_median_odd(self, mocker):
        """Create random data and check it."""
        controller = InputController()
        mocker.patch.object(controller, "data", new=[1, 2, 3, 4, 5])
        controller.calculate_median()

        result = controller.get_result()
        assert len(result) == 1
        assert result["Median"] == 3

    def test_calculate_median_even(self, mocker):
        """Create random data and check it."""
        controller = InputController()
        mocker.patch.object(controller, "data", new=[1, 2, 3, 3, 4, 5])
        controller.calculate_median()

        result = controller.get_result()
        assert len(result) == 1
        assert result["Median"] == 3

    def test_calculate_arithmetic_mean(self, mocker):
        """Create random data and check it."""
        controller = InputController()
        mocker.patch.object(controller, "data", new=[1, 2, 3, 3, 4, 5])
        controller.calculate_arithmetic_mean()

        result = controller.get_result()
        assert len(result) == 1
        assert result["ArithmeticMean"] == 3

    def test_calculate_mean_absolute_deviation(self, mocker):
        """Create random data and check it."""
        controller = InputController()
        mocker.patch.object(controller, "data", new=[1, 2, 3, 3, 4, 5])
        controller.calculate_mean_absolute_deviation()

        result = controller.get_result()
        assert len(result) == 2
        assert round(result["MeanAbsoluteDeviation"], 10) == 1.2909944487

    def test_calculate_standard_deviation(self, mocker):
        """Create random data and check it."""
        controller = InputController()
        mocker.patch.object(controller, "data", new=[1, 2, 3, 3, 4, 5])
        controller.calculate_standard_deviation()

        result = controller.get_result()
        assert len(result) == 2
        assert result["StandardDeviation"] == 1.0

    def test_calculate_all(self, mocker):
        """Create random data and check it."""
        controller = InputController()
        mocker.patch.object(controller, "data", new=[1, 2, 3, 3, 4, 5])
        controller.calculate_minimum()
        controller.calculate_maximum()
        controller.calculate_mode()
        controller.calculate_median()
        controller.calculate_arithmetic_mean()
        controller.calculate_mean_absolute_deviation()
        controller.calculate_standard_deviation()

        result = controller.get_result()
        #pylint: disable=R0801
        #Similar lines in 2 files
        assert len(result) == 7
        assert result["Minimum"] == 1
        assert result["Maximum"] == 5
        assert result["Mode"] == 3
        assert result["Median"] == 3
        assert result["ArithmeticMean"] == 3
        assert round(result["MeanAbsoluteDeviation"], 10) == 1.2909944487
        assert result["StandardDeviation"] == 1.0

    def test___str__(self, mocker):
        """Create random data and check it."""
        controller = InputController()
        mocker.patch.object(controller, "data", new=[1, 2, 3, 4, 5])
        string = str(controller)

        assert string == "[1, 2, 3, 4, 5]"
