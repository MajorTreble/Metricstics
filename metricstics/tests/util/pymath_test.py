"""Test Module for pymath."""
import math
import builtins
import pytest
from metricstics.src.util import pymath


class TestPymath:
    """Test Pymath."""

    def test_sum(self):
        """Generate list or values and sum it."""
        values = {100, 200, 300, 400, 999}

        assert pymath.sum(values) == builtins.sum(values)

    def test_sqrt(self):
        """Test against several numbers."""
        with pytest.raises(ValueError) as excinfo:
            pymath.sqrt(-1)
        assert str(excinfo.value) == "math domain error"

        assert pymath.sqrt(0) == math.sqrt(0)
        assert pymath.sqrt(1) == math.sqrt(1)
        assert pymath.sqrt(4) == math.sqrt(4)

        large_number = 37182.68346312729
        assert round(pymath.sqrt(large_number), 10) == round(
            math.sqrt(large_number), 10
        )

    def test_abs(self):
        """Test against several numbers."""
        assert pymath.abs(-999999) == builtins.abs(-999999)
        assert pymath.abs(-1) == builtins.abs(-1)
        assert pymath.abs(0) == builtins.abs(0)
        assert pymath.abs(1) == builtins.abs(1)
        assert pymath.abs(999999) == builtins.abs(999999)
