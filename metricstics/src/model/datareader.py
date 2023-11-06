"""Reading operations performed on a file."""

# pylint: disable=too-few-public-methods
class DataReader:
    """Interface for Reading data."""
    def read_data(self):
        """Performing read data operation from a file

            Returns:
                 list
        """
        data_lst = []
        try:
            with open("/Users/hetdalal/Documents/GitHub/Metricstics/metricstics/src/model/random_data.txt",
                      "r+", encoding="utf-8") as file1:
                for line in file1:
                    data = ""
                    for char in line:
                        if char == '\n':
                            data_lst.append(float(data))
                        else:
                            data += char
        except FileNotFoundError:
            print("File path not found.")
        return data_lst



