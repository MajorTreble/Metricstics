"""Calculations performed on a data set."""
import math


class Calculation:
    """Interface for Calculation."""

    def calculate_minimum(self,data,result):
        """
                Perform minimum calculation.

                Arg:
                    data(list): the data to work with
                    result(dic): store the result
                """
        data = [5,41,28,9,1]
        min = data[0]

        size = len(data)
        if size == 0:
            result["Minimum"] = 0
            return

        for i in data:
            if i < min:
                min = data

        result["Minimum"] = min
    
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

        result["ArithmeticMean"] = sum(data) / size

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

        result["MeanAbsoluteDeviation"] = math.sqrt(total / size)

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
