"""The controllers in an MVC architecture."""
import random
from metricstics.src.model.calculation import Calculation
from metricstics.src.util.datareader import DataReader
from metricstics.src.util.datareader import ReadResult


class InputController:
    """Handle input actions from the user."""

    def __init__(self):
        """
        Initialize with an empty data list.

        Attributes:
            data (list): The working data list of numbers
            read_result (ReadResult): The status of the read from file
            result (dic): The calculation results
            calc (Calculation): The calculation object
        """
        self.data = []
        self.read_result = ReadResult.NONE
        self.result = {}
        self.calc = Calculation()

    def get_data(self):
        """Get data."""
        return self.data

    def get_read_result(self):
        """Get read result."""
        return self.read_result

    def get_result(self):
        """Get result."""
        return self.result

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
        """Create a list of calculations and perform them."""
        self.calc.calculate_minimum(self.data, self.result)

    def calculate_maximum(self):
        """Create a list of calculations and perform them."""
        self.calc.calculate_maximum(self.data, self.result)

    def calculate_mode(self):
        """Create a list of calculations and perform them."""
        self.calc.calculate_mode(self.data, self.result)

    def calculate_median(self):
        """Create a list of calculations and perform them."""
        self.calc.calculate_median(self.data, self.result)

    def calculate_arithmetic_mean(self):
        """Create a list of calculations and perform them."""
        self.calc.calculate_arithmetic_mean(self.data, self.result)

    def calculate_mean_absolute_deviation(self):
        """Create a list of calculations and perform them."""
        self.calc.calculate_mean_absolute_deviation(self.data, self.result)

    def calculate_standard_deviation(self):
        """Create a list of calculations and perform them."""
        self.calc.calculate_standard_deviation(self.data, self.result)

    def calculate_all(self):
        """Create a list of calculations and perform them."""
        self.calc.calculate_minimum(self.data, self.result)
        self.calc.calculate_maximum(self.data, self.result)
        self.calc.calculate_mode(self.data, self.result)
        self.calc.calculate_median(self.data, self.result)
        self.calc.calculate_arithmetic_mean(self.data, self.result)
        self.calc.calculate_mean_absolute_deviation(self.data, self.result)
        self.calc.calculate_standard_deviation(self.data, self.result)

    def __str__(self):
        """Return the set as the string."""
        return str(self.data)
