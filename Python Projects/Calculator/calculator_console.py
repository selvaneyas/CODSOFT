class ConsoleCalculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2

    def run(self):
        print("Welcome to Simple Calculator!")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = self.add(num1, num2)
        elif operation == '-':
            result = self.subtract(num1, num2)
        elif operation == '*':
            result = self.multiply(num1, num2)
        elif operation == '/':
            result = self.divide(num1, num2)
        else:
            result = "Error: Invalid operation"

        print("Result:", result)


if __name__ == "__main__":
    calculator = ConsoleCalculator()
    calculator.run()
