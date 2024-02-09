import tkinter as tk
from tkinter import ttk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
calculator = tk.Tk()
calculator.title("Stylish Calculator")

# Entry widget to display input and results
entry = tk.Entry(calculator, width=16, font=('Arial', 20), justify='right', bd=5)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Define button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place stylish buttons
style = ttk.Style()
style.configure('TButton', font=('Arial', 14), padding=10)

for (text, row, column) in buttons:
    btn = ttk.Button(calculator, text=text, style='TButton',
                     command=lambda t=text: button_click(t) if t not in {'=', 'C'} else calculate_result() if t == '=' else clear_entry())
    btn.grid(row=row, column=column, padx=5, pady=5)

# Start the main loop
calculator.mainloop()
