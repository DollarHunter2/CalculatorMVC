#-------------------calculatorControll----------------------
from calculator_model import CalculatorModel
from calculator_view import CalculatorView
import math
import tkinter.simpledialog as sd


class CalculatorController:
    def __init__(self, root):
        # create model and view
        self.model = CalculatorModel()
        self.view = CalculatorView(root, self)
    
    # ------------------- INPUT HANDLERS -------------------
    def on_button_click(self, char):
        """Handle any normal button press"""
        value = self.model.add_to_expression(char)
        self.view.update_display(value)

    def on_clear(self):
        value = self.model.clear_all()
        self.view.update_display(value)

    def on_delete(self):
        value = self.model.delete_last()
        self.view.update_display(value)

    def on_equal(self):
        result = self.model.evaluate()
        self.view.update_display(result)

    def temp_convert1(self):
        result = self.model.celsius_to_kelvin()
        self.view.update_display(result)

    def temp_convert2(self):
        result = self.model.kelvin_to_celsius()
        self.view.update_display(result)
    # ------------------- FUNCTION HANDLERS -------------------
    def on_factorial(self):
        result = self.model.factorial()
        self.view.update_display(result)

    def on_sin(self):
        result = self.model.trig_sin()
        self.view.update_display(result)

    def on_cos(self):
        result = self.model.trig_cos()
        self.view.update_display(result)

    def on_tan(self):
        result = self.model.trig_tan()
        self.view.update_display(result)

    def on_cot(self):
        result = self.model.trig_cot()
        self.view.update_display(result)

    def raise_power (self, power):
        try:
            val = float(self.model.expression)
            result = val ** power
            result = self.model.fmt(result)
            self.model.expression = result
            self.view.update_display(result)
        except Exception:
            self.model.expression = ""
            self.view.update_display("Error")
    def ten_power(self):
            try:
                val = float(self.model.expression)
                result = 10 ** val
                result = self.model.fmt(result)
                self.model.expression = result
                self.view.update_display(result) 
            except Exception:
                self.model.expression = ""
                self.view.update_display("ERROR")

    def log10(self):
        try:
            val = float(self.model.expression)
            result = math.log10(val)
            result =self.model.fmt(result)
            self.model.expression = result
            self.view.update_display(result)
        except Exception:
            self.model.expression = ""
            self.view.update_display("ERROR")
    def ln(self):
        try:
            val = float(self.model.expression)
            result = math.log(val)
            result = self.model.fmt(result)
            self.model.expression = result
            self.view.update_display(result)
        except Exception:
            self.model.expression =""
            self.view.update_display("ERROR") 

    def raise_power_dynamic(self):
        try:
            n =sd.askfloat("Exponent","Enter the power n:")
            val = float(self.model.expression)
            result = val**n
            result = self.model.fmt(result)   
            self.model.expression = result
            self.view.update_display(result)
        except Exception:
            self.model.expression = ""
            self.view.update_display("ERROR")

    def on_sign_change(self):
        try:
            val = float(self.model.expression)
            val = -val
            result = self.model.fmt(val)
            self.model.expression = result
            self.view.update_display(result)
        except Exception:
            self.model.expression = ""
            self.view.update_display("ERROR")
        

    def on_percent(self):
        try:
            val = float(self.model.expression)
            val = val / 100
            result = self.model.fmt(val)  
            self.model.expression = result
            self.view.update_display(result)
        except Exception:
            self.model.expression = ""
            self.view.update_display("ERROR")
        
    def nth_raise_power_dynamic(self):
        try:
            n =sd.askfloat("n -th root","Enter the root n:")
            val = float(self.model.expression)
            result = val**(1/n)
            result = self.model.fmt(result)
            self.model.expression = result
            self.view.update_display(result)
        except Exception:
            self.model.expression = ""
            self.view.update_display("ERROR")

    def on_modulo(self):
        try:
            result = eval(self.model.expression.replace('%','%')) #computes modulo
            result= self.model.fmt(result)
            self.model.expression = result

            self.view.update_display(result)
        except Exception:
            self.model.expression = ""
            self.view.update_display("ERROR")

    