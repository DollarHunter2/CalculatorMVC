import tkinter as tk
from calculator_controller import CalculatorController
from PIL import Image, ImageTk

def main():
    root = tk.Tk()
    root.resizable(False, False)

    # Correct icon path
    icon = ImageTk.PhotoImage(
        Image.open(r"C:\Users\cellusys\Desktop\Scientific-calculator-MVC-structure-\My_calculator\calculator image.png")
    )
    root.iconphoto(False, icon)

    app = CalculatorController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
