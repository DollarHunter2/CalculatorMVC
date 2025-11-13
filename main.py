import tkinter as tk
from calculator_controller import CalculatorController
from PIL import Image, ImageTk

def main():
    root = tk.Tk()

    root.geometry("400x600")
    root.resizable(False, False)
    icon = ImageTk.PhotoImage (Image.open(r"C:\Users\Cellusys CodeCamp\Desktop\Joe(vs project)\Scientific-calculator-MVC-structure-\assets sy\calculator image.png"))
    root.iconphoto(False, icon)
    app = CalculatorController(root)
    root.mainloop()

if __name__ == "__main__":
    main()