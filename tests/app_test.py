import pytest

from src.app import my_function

class TestSimpleClass(object):

    def test_my_function(self):
        assert(my_function(1, 1) == 2)
        assert(my_function(1, -1) == 0)
        assert(my_function(0, 0) == 0)
        assert(my_function(-1, -1) == -2)
        assert(my_function(1.0, 1) == 2)
        assert(my_function(1.1, 1.1) == 2.2)
