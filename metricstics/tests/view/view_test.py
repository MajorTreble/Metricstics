"""Test Module for view."""
from tkinter import Tk
from metricstics.src.view.view import View

# pylint: disable=R0903
# Too few public methods (1/2) (too-few-public-methods)


class TestView:
    """Test View."""

    def test_is_window_shown(self):
        """Create empty data and check it."""
        tk = Tk()
        # pylint: disable=unused-variable
        view = View(tk)
        tk.update()

        assert tk.winfo_viewable()
