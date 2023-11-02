"""Test Module for the app"""
from metricstics.src.app import App

# pylint: disable=R0903
# Too few public methods (1/2) (too-few-public-methods)


class TestSimpleClass:
    """Test class"""

    def test_app(self):
        """Test App"""
        app = App()
        assert app.controller is not None
        assert app.view is not None
