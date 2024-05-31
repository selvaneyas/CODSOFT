import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  # Ensure you have Pillow installed

class BasicCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Basic Calculator")
        self.geometry("350x725")
        self.resizable(0, 0)

        self.expression = ""
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display expressions and results
        self.entry = tk.Entry(self, font=("Arial", 20), bd=10, insertwidth=2, width=22, borderwidth=10)
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        # Label to display information about the calculator
        self.info_label = tk.Label(self, text="Basic Calculator: Supports addition, subtraction, multiplication, division, and decimal operations.", font=("Arial", 12), wraplength=350, justify="center")
        self.info_label.grid(row=6, column=0, columnspan=4, pady=10)

        # Notification box to display old expression
        self.notification_label = tk.Text(self, font=("Arial", 10), width=45, height=1, state=tk.DISABLED)
        self.notification_label.grid(row=7, column=0, columnspan=4, pady=5)

        # History box to display expression history
        self.history_label = tk.Text(self, font=("Arial", 10), width=45, height=3)
        self.history_label.grid(row=8, column=0, columnspan=4, pady=5)

        # Button to clear history
        clear_button = tk.Button(self, text="Clear History", command=self.clear_history)
        clear_button.grid(row=9, column=0, columnspan=4, pady=5)

        # Button layout with corresponding image files
        button_info = [
            ("7", "images/button7.png", 1, 0), ("8", "images/button8.png", 1, 1), ("9", "images/button9.png", 1, 2), ("/", "images/div.png", 1, 3),
            ("4", "images/button4.png", 2, 0), ("5", "images/button5.png", 2, 1), ("6", "images/button6.png", 2, 2), ("*", "images/mul.png", 2, 3),
            ("1", "images/button1.png", 3, 0), ("2", "images/button2.png", 3, 1), ("3", "images/button3.png", 3, 2), ("-", "images/sub.png", 3, 3),
            ("0", "images/button0.png", 4, 0), (".", "images/dot.png", 4, 1), ("+", "images/add.png", 4, 2), ("=", "images/equal.png", 4, 3),
            ("C", "images/clear.png", 5, 0), ("←", "images/backspace.png", 5, 1)  # Adding the backspace button
        ]

        for (text, image_file, row, col) in button_info:
            image = Image.open(image_file)
            image = image.resize((50, 50), Image.LANCZOS)  # Resize image to 50x50 pixels
            photo = ImageTk.PhotoImage(image)
            button = tk.Button(self, image=photo, command=lambda txt=text: self.on_button_click(txt))
            button.image = photo  # Keep a reference to avoid garbage collection
            button.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)  # Adjust padding for better layout

    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        elif char == "C":
            self.clear()
        elif char == "←":
            self.backspace()
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

    def backspace(self):
        self.expression = self.expression[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def calculate(self):
        try:
            old_expression = self.expression
            result = eval(self.expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
            self.expression = str(result)

            # Update history
            self.history.append(old_expression)
            self.history_label.delete(1.0, tk.END)
            for expr in self.history:
                self.history_label.insert(tk.END, expr + "\n")

            # Display old expression in notification box
            self.notification_label.config(state=tk.NORMAL)
            self.notification_label.delete(1.0, tk.END)
            self.notification_label.insert(tk.END, f"Previous expression: {old_expression}")
            self.notification_label.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")

    def clear_history(self):
        self.history = []
        self.history_label.delete(1.0, tk.END)

if __name__ == "__main__":
    app = BasicCalculator()
    
    # Window Icon
    window_icon = ImageTk.PhotoImage(file="images/calculator.png")
    app.iconphoto(False, window_icon)
    app.mainloop()
