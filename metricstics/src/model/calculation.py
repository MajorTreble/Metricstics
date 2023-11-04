"""Calculations performed on a data set."""
import metricstics.src.util.pymath as pymath


class Calculation:
    """Interface for Calculation."""

    def calculate_arithmetic_mean(self, data, result):
        """
        Perform the Arithmetic Mean calculation.

        Arg:
            data(set): the data to work with
            result(dic): store the result
        """
        size = len(data)
        if size == 0:
            result["ArithmeticMean"] = 0
            return

        result["ArithmeticMean"] = pymath.sum(data) / size

    def calculate_mean_absolute_deviation(self, data, result):
        """
        Perform the Mean Absolute Deviation calculation.

        Arg:
            data(set): the data to work with
            result(dic): store the result
        """
        size = len(data)
        if size == 0:
            result["MeanAbsoluteDeviation"] = 0
            return

        self.calculate_arithmetic_mean(data, result)
        mean = result["ArithmeticMean"]

        total = 0
        for f in data:
            total += (f - mean) ** 2

        result["MeanAbsoluteDeviation"] = pymath.sqrt(total / size)

    def calculate_standard_deviation(self, data, result):
        """
        Perform the Standard Deviation calculation.

        Arg:
            data(set): the data to work with
            result(dic): store the result
        """
        size = len(data)
        if size == 0:
            result["StandardDeviation"] = 0
            return

        self.calculate_arithmetic_mean(data, result)
        mean = result["ArithmeticMean"]

        total = 0
        for f in data:
            total += abs(f - mean)

        result["StandardDeviation"] = total / size
