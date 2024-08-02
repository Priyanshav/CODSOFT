import tkinter as tk


def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=50, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for button_text, row, col in buttons:
    if button_text == '=':
        button = tk.Button(root, text=button_text, padx=20, pady=10, command=calculate)
    else:
        button = tk.Button(root, text=button_text, padx=20, pady=10, command=lambda symbol=button_text: button_click(symbol))
    button.grid(row=row, column=col, padx=5, pady=5)


root.mainloop()
