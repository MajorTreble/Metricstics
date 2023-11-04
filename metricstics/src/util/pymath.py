"""App is the starting point and contains the main loop"""
import math


def sum(list):
    """Sum up numbers over an iterator"""
    total = 0
    for x in iter(list):
        total += x
    return total


def sqrt(x):
    """Find the square root of a number"""
    return math.sqrt(x)
