import tkinter as tk

class GuiCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.num1_label = tk.Label(master, text="Enter the first number:")
        self.num1_label.pack()

        self.num1_entry = tk.Entry(master)
        self.num1_entry.pack()

        self.num2_label = tk.Label(master, text="Enter the second number:")
        self.num2_label.pack()

        self.num2_entry = tk.Entry(master)
        self.num2_entry.pack()

        self.operation_label = tk.Label(master, text="Enter the operation (+, -, *, /):")
        self.operation_label.pack()

        self.operation_entry = tk.Entry(master)
        self.operation_entry.pack()

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_entry.get()

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    result = "Error: Division by zero"
                else:
                    result = num1 / num2
            else:
                result = "Error: Invalid operation"

            self.result_label.config(text="Result: " + str(result))
        except ValueError:
            self.result_label.config(text="Error: Invalid input")


if __name__ == "__main__":
    root = tk.Tk()
    gui_calculator = GuiCalculator(root)
    root.mainloop()
