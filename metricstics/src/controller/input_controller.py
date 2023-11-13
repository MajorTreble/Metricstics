"""The controllers in an MVC architecture."""
import random
from metricstics.src.model.calculation import Calculation
from metricstics.src.util.datareader import DataReader
from metricstics.src.util.datareader import ReadResult


class InputController:
    """Handle input actions from the user."""

    data = []
    read_result = ReadResult.NONE

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

    def read_data(self, path):
        """Perform read data operation."""
        drobj = DataReader()
        self.read_result = drobj.read_data(path, self.data)

    def calculate_minimum(self):
        """Create a list of calculations and perform them.

        Returns:
            result(dict): The results of the calculations
        """
        result = {}
        calc = Calculation()
        calc.calculate_minimum(self.data, result)
        return result

    def calculate_maximum(self):
        """Create a list of calculations and perform them.

        Returns:
            result(dict): The results of the calculations
        """
        result = {}
        calc = Calculation()
        calc.calculate_maximum(self.data, result)
        return result

    def calculate_mode(self):
        """Create a list of calculations and perform them.

        Returns:
            result(dict): The results of the calculations
        """
        result = {}
        calc = Calculation()
        calc.calculate_mode(self.data, result)
        return result

    def calculate_arithmetic_mean(self):
        """Create a list of calculations and perform them.

        Returns:
            result(dict): The results of the calculations
        """
        result = {}
        calc = Calculation()
        calc.calculate_arithmetic_mean(self.data, result)
        return result

    def calculate_mean_absolute_deviation(self):
        """Create a list of calculations and perform them.

        Returns:
            result(dict): The results of the calculations
        """
        result = {}
        calc = Calculation()
        calc.calculate_mean_absolute_deviation(self.data, result)
        return result

    def calculate_standard_deviation(self):
        """Create a list of calculations and perform them.

        Returns:
            result(dict): The results of the calculations
        """
        result = {}
        calc = Calculation()
        calc.calculate_standard_deviation(self.data, result)
        return result

    def calculate_median(self):
        """Create a list of calculations and perform them.

        Returns:
            result(dict): The results of the calculations
        """
        result = {}
        calc = Calculation()
        calc.calculate_median(self.data, result)
        return result

    def __str__(self):
        """Return the set as the string."""
        return str(self.data)
