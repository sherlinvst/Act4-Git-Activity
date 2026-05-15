# simple calculator that handle arithmetic operations to showcase collaboration using git and Github

# Functions for operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
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