"""Utility file for helper operations for METRICSTICS"""


def sort(data):
    """
    Sort the dataset to find the Median

    Arg:
        data(list): the data to sort
    """
    size = len(data)
    for i in range(size):
        flag = False
        for j in range(0, size - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = True
        if not flag:
            break
    return data
