# Calculator App using Python Tkinter Library
# By: Syed Hassnat Ali

import tkinter as tk

# Calculator App
def press(key):
    entry_text.set(entry_text.get() + str(key))

def clear():
    entry_text.set("")

def calculate():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except:
        entry_text.set("error")

# GUI setup
root = tk.Tk()
root.title("Calculator")

entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, width=20, font=('Arial', 24), bd=10, insertwidth=2, bg="powder blue",
                 justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: press(x) if x not in ['C', '='] else calculate() if x == '=' else clear()
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
