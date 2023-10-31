"""Test Module for a sample function"""
from src.app import my_function

# pylint: disable=R0903
# Too few public methods (1/2) (too-few-public-methods)

class TestSimpleClass():
    """Test class"""

    def test_my_function(self):
        """Test sample function"""
        assert my_function(1, 1) == 2
        assert my_function(1, -1) == 0
        assert my_function(0, 0) == 0
        assert my_function(-1, -1) == -2
        assert my_function(1.0, 1) == 2
        assert my_function(1.1, 1.1) == 2.2
