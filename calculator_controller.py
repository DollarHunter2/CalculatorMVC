#-------------------calculatorControll----------------------
from calculator_model import CalculatorModel
from calculator_view import CalculatorView

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

    def on_sqrt(self):
        result = self.model.square_root()
        self.view.update_display(result)

    def on_cuberoot(self):
        result = self.model.cube_root()
        self.view.update_display(result)

    def on_sign_change(self):
        result = self.model.change_sign()
        self.view.update_display(result)

    def on_percent(self):
        result = self.model.percent()
        self.view.update_display(result)