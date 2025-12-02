from calculator_model import CalculatorModel
from calculator_view import CalculatorView

class CalculatorController:
    def __init__(self, root):
        self.model = CalculatorModel()
        self.view = CalculatorView(root, self)

    # ------------------- BUTTON HANDLERS -------------------
    def on_button_click(self, char, pretty_char=None):
        self.model.add_to_expression(char, pretty_char)
        self.view.update_display(pretty_expressions=self.model.display_exp)

    def on_clear(self):
        value = self.model.clear_all()
        self.view.update_display(pretty_expressions=value, result="")  # fully clears display

    def on_delete(self):
        value = self.model.delete_last()
        self.view.update_display(pretty_expressions=self.model.display_exp, result="")

    def on_equal(self):
        result = self.model.evaluate()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    def on_enter(self, event=None):
        self.on_equal()

    # ------------------- FUNCTION HANDLERS -------------------
    def on_factorial(self):
        result = self.model.factorial()
        self.view.update_display(result=result)

    def on_sin(self):
        result = self.model.trig_sin()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    def on_cos(self):
        result = self.model.trig_cos()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    def on_tan(self):
        result = self.model.trig_tan()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    def on_cot(self):
        result = self.model.trig_cot()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    def on_sqrt(self):
        result = self.model.square_root()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    def on_cuberoot(self):
        result = self.model.cube_root()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    def on_sign_change(self):
        result = self.model.change_sign()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    # ------------------- TEMPERATURE -------------------
    def temp_convert1(self):
        result = self.model.celsius_to_kelvin()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    def temp_convert2(self):
        result = self.model.kelvin_to_celsius()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    # ------------------- NEW FUNCTION HANDLERS -------------------
    def on_abs(self):
        result = self.model.func_abs()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    def on_ln(self):
        result = self.model.func_ln()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    def on_log10(self):
        result = self.model.func_log10()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    def on_exp(self):
        result = self.model.func_exp()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    def on_inverse(self):
        result = self.model.func_inverse()
        self.view.update_display(pretty_expressions=self.model.display_exp, result=result)

    # ------------------- KEYBOARD HANDLERS -------------------
    def on_key_press(self, event):
        char = event.char
        if char in '0123456789+-*/%().':
            self.on_button_click(char)
        elif event.keysym == 'Return':
            self.on_equal()
        elif event.keysym == 'BackSpace':
            self.on_delete()
        elif event.keysym == 'Escape':
            self.on_clear()
