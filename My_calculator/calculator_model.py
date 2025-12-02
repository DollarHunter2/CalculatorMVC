import math

class CalculatorModel:
    def __init__(self):
        self.expression = ""
        self.display_exp = ""
        self.last_pressed_function = False  # Tracks if last action was a function

    # ------------------- EXPRESSION HANDLING -------------------
    def add_to_expression(self, char, pretty_char=None):
        # Reset expression if previous action was a function
        if self.last_pressed_function:
            self.expression = ""
            self.display_exp = ""
            self.last_pressed_function = False

        self.expression += str(char)

        if pretty_char is None:
            mapping = {
                '**2': '²',
                '**3': '³',
                '**(-1)': '⁻¹',
                '10**': '10^',
                '//': '÷',
                '/': '/',
                '*': '×',
                '-': '−',
                '+': '+',
                '%': '%',
                "math.exp(" :'e^',
                "math.log(":'log(',
                "math.log10(":'log₁₀(',
                "**(1/":'X(1/',
                "**(1/n)":"√"
            }
            pretty_char = mapping.get(str(char), str(char))

        self.display_exp += pretty_char
        return self.expression

    def clear_all(self):
        self.expression = ""
        self.display_exp = ""
        self.last_pressed_function = False
        return self.expression

    def delete_last(self):
        if self.expression:
            self.expression = self.expression[:-1]
        if self.display_exp:
            self.display_exp = self.display_exp[:-1]
        return self.expression

    # ------------------- CALCULATION -------------------
    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
            self.last_pressed_function = True
            return result
        except Exception:
            self.expression = ""
            self.display_exp = ""
            return "ERROR"

    def factorial(self):
        try:
            value = int(self.expression)
            result = str(math.factorial(value))
            self.expression = result
            self.display_exp = result
            self.last_pressed_function = True
            return result
        except Exception:
            self.expression = ""
            self.display_exp = ""
            return "ERROR"

    # ------------------- TRIG FUNCTIONS -------------------
    def _trig_func(self, func, name):
        try:
            val = float(self.expression)
            result = str(func(math.radians(val)))
            self.display_exp = f"{name}({self.expression})"
            self.expression = result
            self.last_pressed_function = True
            return result
        except Exception:
            self.expression = ""
            self.display_exp = ""
            return "ERROR"

    def trig_sin(self):
        return self._trig_func(math.sin, "sin")

    def trig_cos(self):
        return self._trig_func(math.cos, "cos")

    def trig_tan(self):
        return self._trig_func(math.tan, "tan")

    def trig_cot(self):
        try:
            val = float(self.expression)
            result = str(1 / math.tan(math.radians(val)))
            self.display_exp = f"cot({self.expression})"
            self.expression = result
            self.last_pressed_function = True
            return result
        except Exception:
            self.expression = ""
            self.display_exp = ""
            return "ERROR"

    # ------------------- ROOTS -------------------
    def square_root(self):
        try:
            val = float(self.expression)
            if val < 0: raise ValueError
            result = str(val ** 0.5)
            self.expression = result
            self.display_exp = result
            self.last_pressed_function = True
            return result
        except Exception:
            self.expression = ""
            self.display_exp = ""
            return "ERROR"

    def cube_root(self):
        try:
            val = float(self.expression)
            result = str(val ** (1/3))
            self.expression = result
            self.display_exp = result
            self.last_pressed_function = True
            return result
        except Exception:
            self.expression = ""
            self.display_exp = ""
            return "ERROR"

    # ------------------- SIGN CHANGE -------------------
    def change_sign(self):
        if self.expression.startswith('-'):
            self.expression = self.expression[1:]
        else:
            self.expression = '-' + self.expression
        return self.expression

    # ------------------- TEMPERATURE -------------------
    def celsius_to_kelvin(self):
        try:
            val = float(self.expression)
            result = str(val + 273.15)
            self.expression = result
            self.last_pressed_function = True
            return result
        except Exception:
            self.expression = ""
            return "ERROR"

    def kelvin_to_celsius(self):
        try:
            val = float(self.expression)
            result = str(val - 273.15)
            self.expression = result
            self.last_pressed_function = True
            return result
        except Exception:
            self.expression = ""
            return "ERROR"

    # ------------------- OTHER FUNCTIONS -------------------
    def func_abs(self):
        try:
            val = float(self.expression)
            result = str(abs(val))
            self.display_exp = f"abs({self.expression})"
            self.expression = result
            self.last_pressed_function = True
            return result
        except:
            self.expression = ""
            self.display_exp = ""
            return "ERROR"

    def func_ln(self):
        try:
            val = float(self.expression)
            result = str(math.log(val))
            self.display_exp = f"ln({self.expression})"
            self.expression = result
            self.last_pressed_function = True
            return result
        except:
            self.expression = ""
            self.display_exp = ""
            return "ERROR"

    def func_log10(self):
        try:
            val = float(self.expression)
            result = str(math.log10(val))
            self.display_exp = f"log10({self.expression})"
            self.expression = result
            self.last_pressed_function = True
            return result
        except:
            self.expression = ""
            self.display_exp = ""
            return "ERROR"

    def func_exp(self):
        try:
            val = float(self.expression)
            result = str(math.exp(val))
            self.display_exp = f"e^({self.expression})"
            self.expression = result
            self.last_pressed_function = True
            return result
        except:
            self.expression = ""
            self.display_exp = ""
            return "ERROR"

    def func_inverse(self):
        try:
            val = float(self.expression)
            result = str(1 / val)
            self.display_exp = f"1/({self.expression})"
            self.expression = result
            self.last_pressed_function = True
            return result
        except:
            self.expression = ""
            self.display_exp = ""
            return "ERROR"
        
    def evaluate(self):
        try:
            # Preprocess expression for trig functions
            expr = self.expression

            # Add multiplication before functions if missing
            import re
            expr = re.sub(r'(\d)(?=sin\()', r'\1*', expr)
            expr = re.sub(r'(\d)(?=cos\()', r'\1*', expr)
            expr = re.sub(r'(\d)(?=tan\()', r'\1*', expr)
            expr = re.sub(r'(\d)(?=cot\()', r'\1*', expr)
            expr = re.sub(r'(\d)(?=abs\()', r'\1*', expr)
            expr = re.sub(r'(\d)(?=ln\()', r'\1*', expr)
            expr = re.sub(r'(\d)(?=log10\()', r'\1*', expr)
            expr = re.sub(r'(\d)(?=math\.exp\()', r'\1*', expr)

            # Replace user-friendly functions with Python math functions
            expr = expr.replace('sin(', 'math.sin(math.radians(')
            expr = expr.replace('cos(', 'math.cos(math.radians(')
            expr = expr.replace('tan(', 'math.tan(math.radians(')
            expr = expr.replace('cot(', '1/math.tan(math.radians(')
            expr = expr.replace('abs(', 'abs(')
            expr = expr.replace('ln(', 'math.log(')
            expr = expr.replace('log10(', 'math.log10(')
            expr = expr.replace('e^(', 'math.exp(')

            # Handle negative numbers with powers: (-2)**2 = 4
            expr = re.sub(r'-(\d+)\*\*', r'(-\1)**', expr)

            result = str(eval(expr))

            # Limit decimal places to 8 digits to fit screen
            if '.' in result:
                result = str(round(float(result), 5))

            self.expression = result
            self.last_pressed_function = True
            return result

        except Exception:
            self.expression = ""
            self.display_exp = ""
            return "ERROR"

