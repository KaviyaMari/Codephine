import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.configure(bg="#2E4057")  # Set background color

        self.length_label = ttk.Label(root, text="Password Length:", foreground="#D9BF77", background="#2E4057")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = ttk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.options_label = ttk.Label(root, text="Character Types:", foreground="#D9BF77", background="#2E4057")
        self.options_label.grid(row=1, column=0, padx=10, pady=10)

        self.use_letters_var = tk.IntVar()
        self.use_letters_checkbox = ttk.Checkbutton(root, text="Letters", variable=self.use_letters_var, style="Checkbutton.TCheckbutton")
        self.use_letters_checkbox.grid(row=1, column=1, padx=10, pady=10)

        self.use_numbers_var = tk.IntVar()
        self.use_numbers_checkbox = ttk.Checkbutton(root, text="Numbers", variable=self.use_numbers_var, style="Checkbutton.TCheckbutton")
        self.use_numbers_checkbox.grid(row=1, column=2, padx=10, pady=10)

        self.use_symbols_var = tk.IntVar()
        self.use_symbols_checkbox = ttk.Checkbutton(root, text="Symbols", variable=self.use_symbols_var, style="Checkbutton.TCheckbutton")
        self.use_symbols_checkbox.grid(row=1, column=3, padx=10, pady=10)

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password, style="TButton")
        self.generate_button.grid(row=2, column=0, columnspan=4, pady=10)

        self.password_label = ttk.Label(root, text="", foreground="#D9BF77", background="#2E4057", font=("Arial", 12))
        self.password_label.grid(row=3, column=0, columnspan=4, pady=10)

        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard, style="TButton")
        self.copy_button.grid(row=4, column=0, columnspan=4, pady=10)

        # Define a custom style for the Checkbuttons
        root.style = ttk.Style()
        root.style.configure("Checkbutton.TCheckbutton", foreground="#D9BF77", background="#2E4057")
        root.style.map("Checkbutton.TCheckbutton", background=[('active', '#40577E')])

        # Define a custom style for the Buttons
        root.style.configure("TButton", foreground="#2E4057", background="#D9BF77", font=("Arial", 12))
        root.style.map("TButton", background=[('active', '#40577E')])

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            use_letters = bool(self.use_letters_var.get())
            use_numbers = bool(self.use_numbers_var.get())
            use_symbols = bool(self.use_symbols_var.get())

            password = self._generate_password(length, use_letters, use_numbers, use_symbols)

            if password:
                self.password_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the password length.")

    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")

    def _generate_password(self, length, use_letters, use_numbers, use_symbols):
        characters = ""
        if use_letters:
            characters += string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character type.")
            return None

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
