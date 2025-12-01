#----------------------------calculatorView-------------------
import tkinter as tk
from PIL import Image, ImageTk 
import re
class CalculatorView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Scientific Calculator (MVC)")
        self.root.configure(bg="#19C6DD", bd=10)
        self.root.resizable(False, False)

    
# --- Display ---
        self.text_input = tk.StringVar()
        self.display = tk.Entry(self.root, font=('sans-serif', 28, 'bold'), textvariable=self.text_input, bd=8, insertwidth=6, bg='#E0E0E0', justify='right')
        self.display.grid(row=0, column=0, columnspan=6, padx=15, pady=25, ipady=25, sticky="ew")
        # ensure row expands
        self.root.grid_rowconfigure(0,weight =1)
        self.root.grid_columnconfigure(0, weight =1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        self.display.xview_moveto(1)

        # Button styles
        self.button_params = {'bd': 1, 'fg': "#000000", 'bg': "#6BBFE1", 'font': ('sans-serif', 20, 'italic')}
        self.button_params_main = {'bd': 1, 'fg': '#000000', 'bg': "#057956", 'font': ('sans-serif', 20,)}

        # Build all buttons
        self.create_buttons()
    #-------------------------INPUT METHOD-------------------
    def on_decimal(self):
        """Add a decimal to current number if it doesnt exist yet"""
        expr = self.controller.model.expression
        last_number = re.split(r'[\+\-\*/\%\(\)]',expr)[-1]
        if "." not in last_number:
            self.controller.on_button_click(".")


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
        add_btn('sin',lambda: self.controller.on_button_click('sin('),2,0)
        add_btn('cos',lambda: self.controller.on_button_click('cos('),2,1)
        add_btn('tan', lambda:self.controller.on_button_click('tan('),2, 2)
        add_btn('cot', lambda:self.controller.on_button_click('cot('),2,3)
        add_btn('π', lambda: self.controller.on_button_click(str(3.14159)), 2, 4)

        # 3rd row
        add_btn('x²', lambda: self.controller.raise_power(2), 3, 0)
        add_btn('x³', lambda: self.controller.raise_power(3), 3, 1)
        add_btn('xⁿ', lambda: self.controller.raise_power_dynamic(), 3, 2) #ask user for n
        add_btn('x⁻¹', lambda: self.controller.raise_power(-1), 3, 3)
        add_btn('10^x', lambda: self.controller.ten_power(), 3, 4)

        # 4th row
        add_btn('√',  lambda: self.controller.raise_power(0.5), 4, 0)
        add_btn('³√',lambda: self.controller.raise_power(1/3), 4, 1)
        add_btn('ⁿ√', lambda: self.controller.nth_root_dynamic(), 4, 2)
        add_btn('log₁₀', lambda: self.controller.log10(), 4, 3)
        add_btn('ln', lambda: self.controller.ln(), 4, 4)

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
             
    ('0', 9, 0),
    ('.', 9, 1),
    ('°C-K', 9, 2),
    ("K-°C",9,3),
    ('=', 9, 4),
    

        ]

        for (text, row, col) in keys:
            if text == 'AC':
                cmd = self.controller.on_clear
            elif text == 'DEL':
                cmd = self.controller.on_delete
            elif text == '=':
                cmd = self.controller.on_equal
            elif text == "°C-K":
                cmd = self.controller.temp_convert1
            elif text =="K-°C":
                cmd = self.controller.temp_convert2
            elif text ==".":
                cmd = self.on_decimal #<----handles decimal
            else:
                cmd = lambda t=text: self.controller.on_button_click(t)
            tk.Button(self.root, text=text, command=cmd, **self.button_params_main).grid(row=row, column=col, sticky="nsew")

    # ------------------- DISPLAY UPDATE -------------------
    def update_display(self, value):
        """Updates the display with the given value"""
        self.text_input.set(str(value))
        self.display.xview_moveto(1)
