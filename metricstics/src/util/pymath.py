"""Pymath implements the necessary math functions."""

# pylint: disable=redefined-builtin


def sum(sequence):
    """Sum up numbers over an iterator."""
    total = 0
    for x in iter(sequence):
        total += x
    return total


def sqrt(x):
    """Find the square root of a number."""
    if x == 0:
        return 0

    if x < 0:
        raise ValueError("math domain error")

    # Find the perfect squares that bracket x
    perfect_square = 0
    while True:
        perfect_square += 1
        next_square = perfect_square + 1
        if x <= next_square * next_square:
            break

    # Iterate on the average of the perfect square and
    # the result until it is close enough or ten times
    result = perfect_square
    count = 0
    while count < 10:
        result = (x / result + result) / 2
        if result * result == x:
            print("Found ", count)
            break
        count += 1

    return result


def abs(x):
    """Find the absolute value of a number."""
    if x < 0:
        return -x
    return x
