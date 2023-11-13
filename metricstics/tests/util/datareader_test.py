"""Test Module for data reader."""
from metricstics.src.util.datareader import DataReader
from metricstics.src.util.datareader import ReadResult


class TestDataReader:
    """Test DataReader."""

    def test_read(self):
        """Test reading froim a file."""
        data_reader = DataReader()
        data = []
        read_result = data_reader.read_data("./data/unittest_data.txt", data)
        print(read_result)

        assert read_result == ReadResult.SUCCESS
        assert len(data) == 3
        assert data[0] == 1.0
        assert data[1] == 2.0
        assert data[2] == 3.0

    def test_read_nofile(self):
        """Test against several numbers."""
        data_reader = DataReader()
        data = []
        read_result = data_reader.read_data("nofile", data)
        assert read_result == ReadResult.NO_FILE
        assert len(data) == 0

    def test_read_nodata(self):
        """Test against several numbers."""
        data_reader = DataReader()
        data = []
        read_result = data_reader.read_data("./data/unittest_empty_data.txt", data)
        assert read_result == ReadResult.NO_DATA
        assert len(data) == 0
