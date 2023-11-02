"""Calculations performed on a data set."""

# pylint: disable=R0903
# Too few public methods (1/2) (too-few-public-methods)


class ArithmeticMean:
    """Calculate the arithmetic mean."""

    def calculate(self, data, result):
        """
        Generate random data.

        Arg:
            data(set): the data to work with
            result(dic): store the result
        """
        size = len(data)
        if size == 0:
            result[str(self)] = 0
            return

        sorted_list = sorted(data)
        index = int(size / 2) - 1

        if size % 2 == 0:
            result[str(self)] = (sorted_list[index] + sorted_list[index + 1]) / 2

        else:
            result[str(self)] = sorted_list[index + 1]

    def __str__(self):
        """Return the name as the string."""
        return "ArithmeticMean"
