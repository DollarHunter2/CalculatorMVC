Title: Scientific Calculator README (MVC)
 

## Overview
This is a  Scientific Calculator implemented in Python, designed using the MVC (Model-View-Controller) architecture. It supports basic and advanced operations, including arithmetic, factorials, powers, roots, trigonometry, logarithms, and exponentials. The project separates concerns for maintainability and scalability.

---

## Features
- Basic arithmetic: `+`, `-`, `*`, `/`
- Scientific functions: factorial, power, square root, trigonometric functions (sin, cos, tan), logarithms (`log`, `ln`), exponentials
- Expression history tracking
- Error handling and validation
- Angle mode selection (Degrees / Radians)
- Clear and backspace functionality
- User-friendly GUI

---

 Project Structure

### Model (CalculatorModel)
Handles all **data, state, and calculations**.

#### Data/State
- `current_input` : string/number  
- `previous_value` : number  
- `selected_operator` : string  
- `expression_history` : list<string>  
- `angle_mode` : enum {DEG, RAD}  
- `error_state` : string/null  

#### Expression Handling
- `append_input(value)` : Add input to current expression  
- `clear()` : Clear current input and reset state  
- `backspace()` : Remove last character of current input  
- `handle_operator(op)` : Handle selected operator  
- `evaluate_expression()` : Compute result of expression  
- `validate_expression()` : Check expression for errors  

#### Scientific Operations
- `factorial(n)` : Compute factorial  
- `power(x, y)` : Compute x^y  
- `sqrt(x)` : Compute square root  
- `trig_sin(x)` : Compute sine (based on angle mode)  
- `trig_cos(x)` : Compute cosine  
- `trig_tan(x)` : Compute tangent  
- `log(x)` / `ln(x)` : Compute logarithms  
- `exp(x)` : Compute exponential  

---

### View (CalculatorView)
Handles **user interface** and **display**.

#### Components
- GUI window with numeric buttons, operators, and scientific function buttons  
- Display for current input and previous calculation  
- Mode selection for DEG/RAD  
- Buttons for clear, backspace, and history viewing  

#### Responsibilities
- Render calculator layout  
- Update display on input or result  
- Pass user interactions to Controller  

---

### Controller (CalculatorController)
Handles **logic and interaction** between View and Model.

#### Responsibilities
- Capture user input from View  
- Update Model state (append input, evaluate expression, handle operator)  
- Handle errors and validation  
- Update View with results or error messages  
- Manage expression history and angle mode changes  

---

## Installation
1. Ensure Python 3.x is installed.  
2. Clone the repository:
```bash
git clone <repository_url>
```
3. Navigate to the project folder:
```bash
cd scientific-calculator
```
4. Install any dependencies (Tkinter is usually included with Python).

---

## Usage
1. Run the calculator:
```bash
python main.py
```
2. Use buttons to input numbers, operators, and scientific functions.  
3. Press `=` to compute results.  
4. Use `C` to clear, and `←` to backspace.  
5. Switch between DEG and RAD for trigonometric functions as needed.

---

## Contributing
- Fork the repository.  
- Create a feature branch:
```bash
git checkout -b feature-branch
```
- Commit changes:
```bash
git commit -m "Add feature"
```
- Push branch:
```bash
git push origin feature-branch
```
- Open a pull request.

---

## License
[MIT License](LICENSE)

---

This README provides a clear MVC-based overview of your Scientific Calculator, explaining the roles of Model, View, and Controller along with usage instructions and scientific operations.
