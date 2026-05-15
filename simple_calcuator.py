# Simple Calculator with Improved Logic

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# Dictionary to map operators to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def get_number(prompt):
    """Safely get a number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Main calculator loop
while True:
    print("\n=== Simple Calculator ===")

    num1 = get_number("Enter first number: ")
    operator = input("Enter operator (+, -, *, /): ")

    # Validate operator first
    if operator not in operations:
        print("Invalid operator. Try again.")
        continue

    num2 = get_number("Enter second number: ")

    # Perform calculation
    result = operations[operator](num1, num2)

    print(f"Result: {result}")

    # Continue or exit
    choice = input("Do another calculation? (y/n): ").lower()

    if choice != "y":
        print("Calculator closed.")
        break