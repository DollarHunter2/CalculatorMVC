#----------------------------calculatorView-------------------
import tkinter as tk
from PIL import Image, ImageTk 
import os
class CalculatorView:
    def __init__(self, root,controller):
        self.root = root
        self.controller = controller
        self.root.title("Scientific calculator")
        self.root.configure(bg="#293C4A")
        #----image loading into the calculator----
       
        img = Image.open(r"C:\Users\Cellusys CodeCamp\Desktop\Joe(vs project)\Scientific-calculator-MVC-structure-\assets sy\calculator image.png")
        img = img.resize((80, 80 ), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(img)
        #-----create label------
        self.logo_label = tk.Label(self.root , image = self.logo)
        self.logo_label.grid(row = 0, column = 0, sticky = "nw", padx = 5, pady = 5 )
        self.logo_label.image = self.logo
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Scientific Calculator")
        self.root.configure(bg="#293C4A", bd=10)

        # --- Display ---
        self.text_input = tk.StringVar()
        self.display = tk.Entry(
            self.root, font=('sans-serif', 20, 'bold'),
            textvariable=self.text_input, bd=5, insertwidth=5,
            bg='#BBB', justify='right'
        )
        self.display.grid(columnspan=5, padx=10, pady=15)

        # Button styles
        self.button_params = {'bd': 5, 'fg': '#BBB', 'bg': '#3C3636', 'font': ('sans-serif', 20, 'bold')}
        self.button_params_main = {'bd': 5, 'fg': '#000', 'bg': '#BBB', 'font': ('sans-serif', 20, 'bold')}

        # Build all buttons
        self.create_buttons()

    # ------------------- BUTTON CREATION -------------------
    def create_buttons(self):
        add_btn = lambda text, cmd, r, c: tk.Button(self.root, text=text, command=cmd, **self.button_params).grid(row=r, column=c, sticky="nsew")

        # 1st row
        add_btn('abs', lambda: self.controller.on_button_click('abs('), 1, 0)
        add_btn('mod', lambda: self.controller.on_button_click('%'), 1, 1)
        add_btn('div', lambda: self.controller.on_button_click('//'), 1, 2)
        add_btn('x!', self.controller.on_factorial, 1, 3)
        add_btn('e', lambda: self.controller.on_button_click(str(2.71828)), 1, 4)

        # 2nd row
        add_btn('sin', self.controller.on_sin, 2, 0)
        add_btn('cos', self.controller.on_cos, 2, 1)
        add_btn('tan', self.controller.on_tan, 2, 2)
        add_btn('cot', self.controller.on_cot, 2, 3)
        add_btn('π', lambda: self.controller.on_button_click(str(3.14159)), 2, 4)

        # 3rd row
        add_btn('x²', lambda: self.controller.on_button_click('**2'), 3, 0)
        add_btn('x³', lambda: self.controller.on_button_click('**3'), 3, 1)
        add_btn('xⁿ', lambda: self.controller.on_button_click('**'), 3, 2)
        add_btn('x⁻¹', lambda: self.controller.on_button_click('**(-1)'), 3, 3)
        add_btn('10^x', lambda: self.controller.on_button_click('10**'), 3, 4)

        # 4th row
        add_btn('√', self.controller.on_sqrt, 4, 0)
        add_btn('³√', self.controller.on_cuberoot, 4, 1)
        add_btn('ⁿ√', lambda: self.controller.on_button_click('**(1/'), 4, 2)
        add_btn('log₁₀', lambda: self.controller.on_button_click('math.log10('), 4, 3)
        add_btn('ln', lambda: self.controller.on_button_click('math.log('), 4, 4)

        # 5th row
        add_btn('(', lambda: self.controller.on_button_click('('), 5, 0)
        add_btn(')', lambda: self.controller.on_button_click(')'), 5, 1)
        add_btn('±', self.controller.on_sign_change, 5, 2)
        add_btn('%', self.controller.on_percent, 5, 3)
        add_btn('e^x', lambda: self.controller.on_button_click('math.exp('), 5, 4)

        # 6th to 9th rows: main keypad
        keys = [
            ('7',6,0), ('8',6,1), ('9',6,2), ('DEL',6,3), ('AC',6,4),
            ('4',7,0), ('5',7,1), ('6',7,2), ('*',7,3), ('/',7,4),
            ('1',8,0), ('2',8,1), ('3',8,2), ('+',8,3), ('-',8,4),
            ('0',9,0), ('.',9,1), ('EXP',9,2), ('=',9,3)
        ]

        for (text, row, col) in keys:
            if text == 'AC':
                cmd = self.controller.on_clear
            elif text == 'DEL':
                cmd = self.controller.on_delete
            elif text == '=':
                cmd = self.controller.on_equal
            else:
                cmd = lambda t=text: self.controller.on_button_click(t)
            tk.Button(self.root, text=text, command=cmd, **self.button_params_main).grid(row=row, column=col, sticky="nsew")

    # ------------------- DISPLAY UPDATE -------------------
    def update_display(self, value):
        """Updates the display with the given value"""
        self.text_input.set(value)
