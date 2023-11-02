"""Test Module for the app"""
import os
from metricstics.src.app import App

# pylint: disable=R0903
# Too few public methods (1/2) (too-few-public-methods)


class TestApp:
    """Test the App"""
    
    def test_app(self):
        """Test App"""
        
        if os.environ.get('DISPLAY','') == '':
            print('no display found. Using :0.0')
            os.environ.__setitem__('DISPLAY', ':0.0')        
        
        app = App()
        assert app.controller is not None
        assert app.view is not None
