"""Reading operations performed on a file."""
class datareader:
    """Interface for Reading data."""
    def read_data(self):
        """Performing read data operation from a file

            Returns:
                 list
        """
        with open("myfile.txt", "r+", encoding="utf-8") as file1:
        # Reading from a file
            data_string = file1.read()

        data_list = data_string.split("\n")
        return data_list
