"""Test Module for view."""
from tkinter import Tk
import os
from metricstics.src.view.view import View

# pylint: disable=R0903
# Too few public methods (1/2) (too-few-public-methods)


class TestView:
    """Test View."""

    def test_is_window_shown(self):
        """Create empty data and check it."""

        if os.environ.get('DISPLAY','') == '':
            # pylint: disable=unnecessary-dunder-call
            print('no display found. Using :0.0')
            os.environ.__setitem__('DISPLAY', ':0.0')

        tk = Tk()
        # pylint: disable=unused-variable
        view = View(tk)
        tk.update()

        assert tk.winfo_viewable()
