import math
import re
class CalculatorModel:
    def __init__(self):
        self.expression = ""

        """Alias to format_smart for backward compatibility"""
    def fmt(self,value):
        return self.format_smart(value)
    @staticmethod
    def format_smart(value):
        """Format number: strip decimals for whole numbers, 5dp for floats"""
        try:
            value = float(value)
            if value.is_integer():
                return str(int(value))
            else:
                return "{:.3f}".format(value)
        except:
            return "ERROR"
    def add_to_expression(self, char):
        """Add a character to the current expression"""
        self.expression += str(char)
        return self.expression

    def clear_all(self):
        """Clear everything"""
        self.expression = ""
        return self.expression

    def delete_last(self):
        """Delete last character"""
        self.expression = self.expression[:-1]
        return self.expression


    def factorial(self):
        """Calculate factorial of current number"""
        try:
            value = (int(float(self.expression)))
            result =(math.factorial(value))
            result = self.fmt(result)
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"

    def trig_sin(self):
        return self._trig_func(math.sin)

    def trig_cos(self):
        return self._trig_func(math.cos)

    def trig_tan(self):
        return self._trig_func(math.tan)

    def trig_cot(self):
        try:
            val = eval(self.expression)
            val = math.radians(float(val))
            tan_val = math.tan(val)
            if tan_val == 0:
                raise ValueError("Cotangent undefined") #prevent ZeoDivision Error
            result = 1/tan_val
            result =self.fmt(result)
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"

        
    def insert_implicit_multiplication(self, expr):
            """
            Insert * automatically in cases like:
            - 6cos(9) → 6*cos(9)
            - 3(4+5) → 3*(4+5)
            - )sin(30) → )*sin(30)
            """
             # number followed by sin, cos, tan, cot
            expr = re.sub(r'(\d)(sin|cos|tan|cot)', r'\1*\2', expr)
    
            # closing bracket followed by trig
            expr = re.sub(r'(\))(sin|cos|tan|cot)', r'\1*\2', expr)
    
            # number followed by (
            expr = re.sub(r'(\d)\(', r'\1*(', expr)
            return expr


    def _trig_func(self, func):
        """Helper for sin, cos, tan"""
        try:
            
            expr = self.insert_implicit_multiplication(self.expression)
            val = eval(expr)
        
            val = math.radians(float(val))
            result = func(val)
            result = self.fmt(result)
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"
        
    def evaluate(self, expr=None):
        """Evaluate expression safely with math functions and return formatted result."""
        
        # Choose expression source
        expr_to_eval = self.expression if expr is None else str(expr)

        # Allowed functions (angles in degrees for trig helpers)
        allowed_names = {
            'sin': lambda x: math.sin(math.radians(x)),
            'cos': lambda x: math.cos(math.radians(x)),
            'tan': lambda x: math.tan(math.radians(x)),
            'cot': lambda x: (1.0 / math.tan(math.radians(x))) if math.tan(math.radians(x)) != 0 else float('inf'),
            'pi': math.pi,
            'e': math.e,
            'sqrt': math.sqrt,
            'log': math.log,      # natural log
            'log10': math.log10,
            'abs': abs
        }

        try:
            # Evaluate expression using only allowed names and no builtins
            expr_fixed = self.insert_implicit_multiplication(self.expression)
            result = eval(expr_fixed, {"__builtins__": {}}, allowed_names)
        except Exception:
            return "ERROR"

        # Format result using existing formatter
        try:
            return self.fmt(result)
        except Exception:
            # Fallback formatting similar to fmt
            try:
                val = float(result)
                if val.is_integer():
                    return str(int(val))
                else:
                    return "{:.3f}".format(val)
            except Exception:
                return str(result)

    def square_root(self):
        return self._root_func(2)

    def cube_root(self):
        return self._root_func(3)

    def _root_func(self, n):
        """Find n-th root of expression"""
        try:
            val = float(self.expression)
            if val < 0:
                raise ValueError
            result = val ** (1 / n)
            result =self.fmt(result)
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"

    def change_sign(self):
        if self.expression.startswith('-'):
            self.expression = self.expression[1:]
        else:
            self.expression = '-' + self.expression
        return self.expression

    def percent(self):
        try:
            result =(float(self.expression) / 100)
            result =self.fmt(result)
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"  
        
    def celsius_to_kelvin(self):
        """Convert Celsius to Kelvin"""
        try:
            val = float(self.expression)
            result = round(val + 273.15,2) #only to 2dp
            result = str(result)
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"
  
            
    def kelvin_to_celsius(self):
        """Convert Kelvin to Celsius"""
        try:
            val = float(self.expression)
            result = round(val - 273.15,2) #--only 2dp
            result = str(result)
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"
