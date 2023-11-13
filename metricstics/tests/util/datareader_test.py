"""Test Module for data reader."""
import pytest
from metricstics.src.util.datareader import DataReader
from metricstics.src.util.datareader import ReadResult


class TestDataReader:
    """Test DataReader."""

    def test_read(self):
        """Test reading froim a file."""
        data_reader = DataReader()
        list = []
        read_result = data_reader.read_data("./data/unittest_data.txt", list)
        print(read_result)

        assert read_result == ReadResult.SUCCESS
        assert len(list) == 3
        assert list[0] == 1.0
        assert list[1] == 2.0
        assert list[2] == 3.0

    def test_read_nofile(self):
        """Test against several numbers."""
        data_reader = DataReader()
        list = []
        read_result = data_reader.read_data("nofile", list)
        assert read_result == ReadResult.NO_FILE
        assert len(list) == 0

    def test_read_nodata(self):
        """Test against several numbers."""
        data_reader = DataReader()
        list = []
        read_result = data_reader.read_data("./data/unittest_empty_data.txt", list)
        assert read_result == ReadResult.NO_DATA
        assert len(list) == 0
