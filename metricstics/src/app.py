"""App is the starting point and contains the main loop"""
from tkinter import Tk
import os
import sys

sys.path.append(os.path.abspath("./"))

# pylint: disable=wrong-import-position
from metricstics.src.controller.input_controller import InputController
from metricstics.src.view.view import View


class App(Tk):
    """Launch the application and create the MVC"""

    def __init__(self):
        """Launch the application and create the MVC"""
        super().__init__()

        self.title("METRICSTICS")
        # self.geometry("720x500")
        # self.configure(background="lightblue")

        # create a view and place it on the root window
        self.view = View(self)
        self.view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        self.controller = InputController()

        # set the controller to view
        self.view.set_controller(self.controller)


if __name__ == "__main__":
    app = App()
    app.mainloop()
