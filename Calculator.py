import tkinter as tk
from tkinter import messagebox

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_operation(operation):
    global first_number, operation_type
    first_number = float(display.get())
    operation_type = operation
    display.delete(0, tk.END)

def button_equal():
    second_number = float(display.get())
    display.delete(0, tk.END)
    try:
        if operation_type == '+':
            result = first_number + second_number
        elif operation_type == '-':
            result = first_number - second_number
        elif operation_type == '*':
            result = first_number * second_number
        elif operation_type == '/':
            result = first_number / second_number
        else:
            result = "Error"
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        return
    display.insert(0, result)

root = tk.Tk()
root.title("Simple Calculator")

display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_list = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 1, 4)
]


for button_text, row, column, *grid_options in button_list:
    if button_text == '=':
        button = tk.Button(root, text=button_text, padx=79, pady=25, command=button_equal)
    elif button_text == 'C':
        button = tk.Button(root, text=button_text, padx=40, pady=25, command=button_clear)
    elif button_text in ('+', '-', '*', '/'):
        button = tk.Button(root, text=button_text, padx=40, pady=25, command=lambda button_text=button_text: button_operation(button_text))
    else:
        button = tk.Button(root, text=button_text, padx=40, pady=25, command=lambda button_text=button_text: button_click(button_text))
    
    
    if grid_options:
        button.grid(row=row, column=column, rowspan=grid_options[0], columnspan=grid_options[1])
    else:
        button.grid(row=row, column=column)

root.mainloop()