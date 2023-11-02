"""Test Module for view."""
from metricstics.src.view.view import View
from tkinter import Tk

# pylint: disable=R0903
# Too few public methods (1/2) (too-few-public-methods)


class TestView:
    """Test View."""

    def test_is_window_shown(self):
        """Create empty data and check it."""
        tk = Tk()
        view = View(tk)
        tk.update()

        assert tk.winfo_viewable() == True
