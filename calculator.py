import tkinter as tk 
import re
import math
from unittest import result

# update expression
def press(num):
    global expression
    if len(expression.replace('.', '').replace('-', '')) >= 12 and expression != "0":
        return
    if expression == "0":
        expression = str(num)
    else:
        expression += str(num)
    equation.set(expression)

# equal function
def equalpress():
    global expression
    try:
        total = eval(expression)  # evaluate expression
        total_str = "{:.12g}".format(total)  # format to max 12 digits, remove trailing zeros
        equation.set(total_str)
        expression = total_str
    except: 
        equation.set("error")
        expression = "0"

# clear function
def clear(): 
    global expression
    expression = "0"
    equation.set("0")

# clear entry function
def clear_entry():
    global expression
    # Remove the last number (digits and optional decimal) from the end of the expression
    expression = re.sub(r'(\d+\.?\d*)$', '', expression)
    # If the expression is empty or ends with an operator, show 0
    if not expression or expression[-1] in '+-*/':
        equation.set(expression + '0')
    else:
        equation.set(expression)
    if not expression:
        expression = "0"

# delete entry function
def delete_entry():
    global expression
    expression = expression[:-1]
    if not expression:
        expression = "0"
    equation.set(expression)

# reciprocal function
def reciprocal():
    global expression
    try:
        value = eval(expression)
        result = 1 / value
        expression = str(result)
        equation.set(expression)
    except Exception:
        equation.set("error")
        expression = "0"

# square function
def square():
    global expression
    try:
        value = eval(expression)
        result = value ** 2
        result = "{:.12g}".format(result)
        expression = result
        equation.set(result)
    except Exception:
        equation.set("error")
        expression = "0"

# square root function
def square_root():
    global expression
    try:
        value = eval(expression)
        result = math.sqrt(value)
        result = "{:.12g}".format(result)
        expression = result
        equation.set(result)
    except Exception:
        equation.set("error")
        expression = "0"

# negate function
def negate():
    global expression
    match = re.search(r'(-?\d+\.?\d*)$', expression)
    if match:
        num_str = match.group(1)
        if num_str != "0":
            start = match.start(1)
            negated = str(-float(num_str))
            expression = expression[:start] + negated
            equation.set(expression)
    else:
        equation.set(expression)

# percent function 
def percent(): 
    global expression
    match = re.search(r'(\d+\.?\d*)$', expression)
    if match:
        num_str = match.group(1)
        start = match.start(1)
        percent_value = str(float(num_str) / 100)
        expression = expression[:start] + percent_value
        equation.set(expression)

# program
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Calculator")
    window.geometry("280x400")
    window.configure(bg = "#252A33")

    equation = tk.StringVar()
    equation.set("0")
    expression = "0"

    # entry field 
    entry_field = tk.Entry(window, textvariable=equation, font=("Arial", 30), bd=3, insertwidth=2, width=16,
                           borderwidth=4, relief="raised", justify="right", bg="#505B6E", fg="white")
    entry_field.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)

    # Configure all rows and columns to expand
    for i in range(7):   # rows 0–6 (entry + 6 button rows)
        window.grid_rowconfigure(i, weight=1)
    for j in range(4):   # 4 columns
        window.grid_columnconfigure(j, weight=1)

    # buttons
    buttons = [
        ('%', 1, 0), ('CE', 1, 1), ('C', 1, 2), ('<-', 1, 3),
        ('1/x', 2, 0), ('x^2', 2, 1), ('√x', 2, 2), ('/', 2, 3),
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
        ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
        ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
        ('+/-', 6, 0), ('0', 6, 1), ('.', 6, 2), ('=', 6, 3),
    ]

    for (text, row, col) in buttons:
        if text == "=":
            btn = tk.Button(window, text=text, bg="#505B6E", fg="white", command=equalpress)
        elif text == "C":
            btn = tk.Button(window, text=text, bg="#505B6E", fg="white", command=clear)
        elif text == "CE":
            btn = tk.Button(window, text=text, bg="#505B6E", fg="white", command=clear_entry)
        elif text == "<-":
            btn = tk.Button(window, text=text, bg="#505B6E", fg="white", command=delete_entry)
        elif text == "1/x":
            btn = tk.Button(window, text=text, bg="#505B6E", fg="white", command=reciprocal)
        elif text == "x^2":
            btn = tk.Button(window, text=text, bg="#505B6E", fg="white", command=square)
        elif text == "√x":
            btn = tk.Button(window, text=text, bg="#505B6E", fg="white", command=square_root)
        elif text == "+/-":
            btn = tk.Button(window, text=text, bg="#505B6E", fg="white", command=negate)
        elif text == "%":
            btn = tk.Button(window, text=text, bg="#505B6E", fg="white", command=percent)
        else:
            btn = tk.Button(window, text=text, bg="#505B6E", fg="white",
                            command=lambda t=text: press(t))
        btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
    
    window.mainloop()




