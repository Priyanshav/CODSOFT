import tkinter as tk
from tkinter import messagebox
import string
import random


def gen_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))


def generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be positive.")
        password = gen_password(length)
        password_var.set(password)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter the desired length of the password:").pack(pady=10)

length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate, fg="magenta").pack(pady=10)

password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Arial", 12, "bold"), fg="blue")
password_label.pack(pady=10)

root.mainloop()
