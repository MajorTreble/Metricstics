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

    def test_calculate(self):
        """Create random data and check it."""
        controller = InputController()
        controller.generate_random_data(5)
        result = controller.calculate()

        assert len(result) == 1

    def test___str__(self):
        """Create random data and check it."""
        controller = InputController()
        controller.generate_random_data(5)
        string = str(controller)

        assert string == "{1, 2, 3, 4, 5}"
