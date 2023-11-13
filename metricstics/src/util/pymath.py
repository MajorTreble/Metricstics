"""App is the starting point and contains the main loop"""
import builtins
import math

# pylint: disable=redefined-builtin


def sum(sequence):
    """Sum up numbers over an iterator"""
    print(sequence)
    total = 0
    for x in iter(sequence):
        total += x
    return total


def sqrt(x):
    """Find the square root of a number"""
    return math.sqrt(x)


def abs(x):
    """Find the square root of a number"""
    return builtins.abs(x)
