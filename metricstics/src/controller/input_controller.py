"""The controllers in an MVC architecture."""
from metricstics.src.model.calculation import ArithmeticMean


class InputController:
    """Handle input actions from the user."""

    def __init__(self):
        """
        Initialize with an empty data set.

        Attributes:
            data (set): The working data set of numbers
        """
        self.data = set()

    def generate_random_data(self, size):
        """
        Generate random data.

        Arg:
            size(int): the length of the data
        """
        self.data = {1, 2, 3, 4, size}

    def clear_data(self):
        """Clear the data set to empty."""
        self.data = set()

    def calculate(self):
        """Create a list of calculations and perform them.

        Returns:
            result(dict): The results of the calculations
        """
        result = {}
        mean = ArithmeticMean()
        mean.calculate(self.data, result)
        return result

    def __str__(self):
        """Return the set as the string."""
        return str(self.data)
