"""Calculations performed on a data set."""

from metricstics.src.util import pymath
from metricstics.src.util import operation


class Calculation:
    """Interface for Calculation."""

    def calculate_minimum(self, data, result):
        """
        Perform minimum calculation.

        Arg:
            data(list): the data to work with
            result(dic): store the result
        """
        size = len(data)
        if size == 0:
            result["Minimum"] = 0
            return

        minimum = data[0]
        for i in data:
            if i < minimum:
                minimum = i

        result["Minimum"] = minimum

    def calculate_maximum(self, data, result):
        """
        Find maximum value.

        Arg:
            data(list): the data to work with
            result(dic): store the result
        """
        size = len(data)
        if size == 0:
            result["Maximum"] = 0
            return

        maximum = data[0]
        for i in data:
            if i > maximum:
                maximum = i

        result["Maximum"] = maximum

    def calculate_mode(self, data, result):
        """
        Find the mode.

        Arg:
            data(list): the data to work with
            result(dic): store the result
        """
        size = len(data)
        if size == 0:
            result["Mode"] = 0
            return

        result["Mode"] = 0

    def calculate_median(self, data, result):
        """
        Find the Median of the set.

        Arg:
        data(list): the data to work with
        result(dict): store the result
        """
        size = len(data)
        if size == 0:
            result["Median"] = 0
            return

        ordered_list = operation.sort(data)
        middle = int(size / 2) - 1

        if size % 2 == 0:
            result["Median"] = (ordered_list[middle] + ordered_list[middle + 1]) / 2

        else:
            result["Median"] = ordered_list[middle + 1]

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
            total += pymath.abs(f - mean)

        result["StandardDeviation"] = total / size
