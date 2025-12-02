import tkinter as tk

class CalculatorView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Scientific Calculator (MVC)")
        self.root.configure(bg="#5AC4D2", bd=10)
        self.root.resizable(True, True)

        # ------------------ DISPLAY ------------------
        self.expression_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.expression_label = tk.Label(
            self.root,
            textvariable=self.expression_var,
            font=('sans-serif', 28),
            fg="#000000",
            anchor='se',   # top-left alignment
            bg="#D8D8D8"
        )
        self.expression_label.grid(row=0, column=0, columnspan=6, sticky='ew', padx=15, pady=(15,0))

        self.result_label = tk.Label(
            self.root,
            textvariable=self.result_var,
            font=('sans-serif', 28, 'bold'),
            fg='black',
            anchor='w',  # bottom-left alignment
            bg="#FFFFFF",
            border=5
        )
        self.result_label.grid(row=1, column=0, columnspan=6, sticky='ew', padx=15, pady=(0,15))

        # ------------------ GRID CONFIG ------------------
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=0)
        for i in range(2, 11):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(6):
            self.root.grid_columnconfigure(j, weight=1)

        # ------------------ BUTTON STYLES ------------------
        self.button_params = {'bd': 1, 'fg': "#000000", 'bg': "#6BBFE1", 'font': ('sans-serif', 20, 'italic')}
        self.button_params_main = {'bd': 1, 'fg': '#000000', 'bg': "#199B74", 'font': ('sans-serif', 20)}

        # ------------------ CREATE BUTTONS ------------------
        self.create_buttons()

        # ------------------ KEYBOARD BINDINGS ------------------
        self.root.bind("<Key>", controller.on_key_press)
        self.root.bind("<Return>", controller.on_enter)

    # ------------------- BUTTON CREATION -------------------
    def create_buttons(self):
        add_btn = lambda text, cmd, r, c: tk.Button(
            self.root, text=text, command=cmd, **self.button_params
        ).grid(row=r, column=c, sticky="nsew", padx=0, pady=0)

        # 1st row (row=2)
        add_btn('abs', self.controller.on_abs, 2, 0)
        add_btn('mod', lambda: self.controller.on_button_click('mod'), 2, 1)
        add_btn('/', lambda: self.controller.on_button_click('/'), 2, 2)
        add_btn('x!', self.controller.on_factorial, 2, 3)
        add_btn('e', lambda: self.controller.on_button_click(str(2.71828)), 2, 4)

        # 2nd row (row=3)
        add_btn('sin', self.controller.on_sin, 3, 0)
        add_btn('cos', self.controller.on_cos, 3, 1)
        add_btn('tan', self.controller.on_tan, 3, 2)
        add_btn('cot', self.controller.on_cot, 3, 3)
        add_btn('π', lambda: self.controller.on_button_click(str(3.14159)), 3, 4)

        # 3rd row (row=4)
        add_btn('x²', lambda: self.controller.on_button_click("**2"), 4, 0)
        add_btn('x³', lambda: self.controller.on_button_click("**3"), 4, 1)
        add_btn('xⁿ', lambda: self.controller.on_button_click("**"), 4, 2)
        add_btn('1/x', self.controller.on_inverse, 4, 3)
        add_btn('10^x', lambda: self.controller.on_button_click("10**"), 4, 4)

        # 4th row (row=5)
        add_btn('√', self.controller.on_sqrt, 5, 0)
        add_btn('∛', self.controller.on_cuberoot, 5, 1)
        add_btn('∜', lambda: self.controller.on_button_click("**(1/"), 5, 2)
        add_btn('ⁿ√', lambda: self.controller.on_button_click("**(1/n)"), 5, 3)
        add_btn('ln', self.controller.on_ln, 5, 4)

        # 5th row (row=6)
        add_btn('(', lambda: self.controller.on_button_click('('), 6, 0)
        add_btn(')', lambda: self.controller.on_button_click(')'), 6, 1)
        add_btn('±', self.controller.on_sign_change, 6, 2)
        add_btn("log₁₀", self.controller.on_log10, 6, 3)
        add_btn('e^x', self.controller.on_exp, 6, 4)

        # 6th to 9th rows: main keypad (row=7-10)
        keys = [
            ('7',7,0), ('8',7,1), ('9',7,2), ('DEL',7,3), ('AC',7,4),
            ('4',8,0), ('5',8,1), ('6',8,2), ('*',8,3), ('÷',8,4),
            ('1',9,0), ('2',9,1), ('3',9,2), ('+',9,3), ('-',9,4),
            ('0',10,0), ('.',10,1), ('C-K',10,2), ("K-C",10,3), ('=',10,4)
        ]

        for text, row, col in keys:
            if text == 'AC':
                cmd = self.controller.on_clear
            elif text == 'DEL':
                cmd = self.controller.on_delete
            elif text == '=':
                cmd = self.controller.on_equal
            elif text == "C-K":
                cmd = self.controller.temp_convert1
            elif text == "K-C":
                cmd = self.controller.temp_convert2
            else:
                cmd = lambda t=text: self.controller.on_button_click(t)
            tk.Button(self.root, text=text, command=cmd, **self.button_params_main).grid(
                row=row, column=col, sticky="nsew", padx=1, pady=2
            )

    # ------------------- DISPLAY UPDATE -------------------
    def update_display(self, result=None, pretty_expressions=None):
        if pretty_expressions is not None:
            self.expression_var.set(pretty_expressions)
        if result is not None:
            self.result_var.set(result)
