"""The controllers in an MVC architecture."""
import random
from metricstics.src.model.calculation import Calculation



class InputController:
    """Handle input actions from the user."""

    data = set()

    def __init__(self):
        """
        Initialize with an empty data set.

        Attributes:
            data (set): The working data set of numbers
        """


    def generate_random_data(self, size):
        """
        Generate random data.

        Arg:
            size(int): the length of the data
        """
        self.data = [random.uniform(0, 1000) for _ in range(size)]

    def clear_data(self):
        """Clear the data set to empty."""
        self.data = []

    def calculate_arithmetic_mean(self):
        """Create a list of calculations and perform them.

        Returns:
            result(dict): The results of the calculations
        """
        result = {}
        mean = Calculation()
        mean.calculate_arithmetic_mean(self.data, result)
        return result

    def calculate_mean_absolute_deviation(self):
        """Create a list of calculations and perform them.

        Returns:
            result(dict): The results of the calculations
        """
        result = {}
        mean = Calculation()
        mean.calculate_mean_absolute_deviation(self.data, result)
        return result

    def calculate_standard_deviation(self):
        """Create a list of calculations and perform them.

        Returns:
            result(dict): The results of the calculations
        """
        result = {}
        mean = Calculation()
        mean.calculate_standard_deviation(self.data, result)
        return result

    def calculate_median(self):
        """Create a list of calculations and perform them.

        Returns:
            result(dict): The results of the calculations
        """
        result = {}
        mean = Calculation()
        mean.calculate_median(self.data, result)
        return result

    def __str__(self):
        """Return the set as the string."""
        return str(self.data)
