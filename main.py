import tkinter as tk
from calculator_controller import CalculatorController

def main():
    root = tk.Tk()
    app = CalculatorController(root)
    root.mainloop()

if __name__ == "__main__":
    main()