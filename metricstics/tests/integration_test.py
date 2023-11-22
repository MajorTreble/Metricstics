"""Integration Test."""
from metricstics.src.controller.input_controller import InputController

# pylint: disable=R0903
# Too few public methods (1/2) (too-few-public-methods)


class TestIntegration:
    """Test with modules integrated together."""

    def test_1000_values(self):
        """Read 1000 entries and compare results."""
        controller = InputController()
        path = "./data/integrationtest_data.txt"
        controller.read_data(path)
        assert len(controller.get_data()) == 1000

        controller.calculate_all()
        result = controller.get_result()
        # pylint: disable=R0801
        # Similar lines in 2 files
        assert len(result) == 7
        assert result["Minimum"] == 1
        assert result["Maximum"] == 997
        assert result["Mode"] == 71
        assert result["Median"] == 492
        assert result["ArithmeticMean"] == 499.457
        assert round(result["MeanAbsoluteDeviation"], 7) == 249.452312
        assert round(result["StandardDeviation"], 7) == 288.2834649
