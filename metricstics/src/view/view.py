"""The views in an MVC architecture."""
from tkinter import Tk, Text

# from tkinter.ttk import *
from tkmacosx import Button

from metricstics.src.controller.input_controller import InputController



root = Tk()


root.title("METRICSTICS")
root.geometry("720x500")
root.configure(background="lightblue")

controller = InputController()


def generate_data_clicked():
    """Command for generate data button."""
    controller.generate_random_data(5)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", controller.data)


def calculate_arithmatic_mean_clicked():
    """Command for calculate arithmatic mean button."""
    result = controller.calculate()
    print(result)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", result["ArithmeticMean"])


buttonRD = Button(root, text="Read Data", borderless=1)
buttonRD.place(x=50, y=50)
buttonGD = Button(
    root, text="Generate Data", borderless=1, command=generate_data_clicked
)
buttonGD.place(x=50, y=100)
buttonVMI = Button(root, text="View Minimum", borderless=1)
buttonVMI.place(x=50, y=150)
buttonVMX = Button(root, text="View Maximum", borderless=1)
buttonVMX.place(x=50, y=200)
buttonVMO = Button(root, text="View Mode", borderless=1)
buttonVMO.place(x=50, y=250)
buttonCM = Button(root, text="Calculate Median", borderless=1)
buttonCM.place(x=450, y=50)
buttonCAM = Button(
    root,
    text="Calculate Arithmatic Mean",
    borderless=1,
    command=calculate_arithmatic_mean_clicked,
)
buttonCAM.place(x=450, y=100)
buttonCSD = Button(root, text="Calculate Standard Deviation", borderless=1)
buttonCSD.place(x=450, y=150)
buttonCMAD = Button(root, text="Calculate Mean Absolute Deviation", borderless=1)
buttonCMAD.place(x=450, y=200)
buttonSR = Button(root, text="Save Results", borderless=1)
buttonSR.place(x=450, y=250)


output_text = Text(root, width=50, height=10)
output_text.place(x=150, y=290)


root.mainloop()
