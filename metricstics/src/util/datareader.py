"""Reading operations performed on a file."""
from enum import Enum


class ReadResult(Enum):
    """Enum with result of read from file."""

    NONE = 0
    SUCCESS = 1
    NO_FILE = 2
    NO_DATA = 3


# pylint: disable=too-few-public-methods
class DataReader:
    """Interface for Reading data."""

    def read_data(self, path, data_list):
        """Read a list of numbers from a file.

        Returns:
             read_result (list): result of the read
        """
        try:
            with open(
                path,
                "r+",
                encoding="utf-8",
            ) as file1:
                for line in file1:
                    data = ""
                    for char in line:
                        if char == "\n":
                            data_list.append(float(data))
                        else:
                            data += char
        except FileNotFoundError:
            return ReadResult.NO_FILE

        if len(data_list) == 0:
            return ReadResult.NO_DATA

        return ReadResult.SUCCESS
