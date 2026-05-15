# simple calculator that handle arithmetic operations to showcase collaboration using git and Github

# Helper validation
def is_number(x):
    return isinstance(x, (int, float))


# Addition
def add(a, b):
    if not (is_number(a) and is_number(b)):
        return "Error: invalid input"
    return a + b


# Subtraction
def subtract(a, b):
    if not (is_number(a) and is_number(b)):
        return "Error: invalid input"
    return a - b


# Multiplication
def multiply(a, b):
    if not (is_number(a) and is_number(b)):
        return "Error: invalid input"
    return a * b


# Division (improved safety)
def divide(a, b):
    if not (is_number(a) and is_number(b)):
        return "Error: invalid input"
    if b == 0:
        return "Error: Division by zero"
    return a / b
    return "Error: Division by zero"

# Main program with while loop
while True:
    # User input
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Call the correct function
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        result = "Invalid operator"

    # Output
    print("Result:", result)

    # Ask user if they want to continue
    choice = input("Do you want to perform another calculation? (yes/no): ").lower()

    if choice != "yes":
        print("Calculator closed.")
        break