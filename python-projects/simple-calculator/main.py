
# Simple Calculator - Python Practice

print("Welcome to the Calculator!")

# Math functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# User input
num1 = float(input("Enter the first number: "))
operation = input("Choose an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Calculate the result
if operation == "+":
    result = add(num1, num2)

elif operation == "-":
    result = subtract(num1, num2)

elif operation == "*":
    result = multiply(num1, num2)

elif operation == "/":
    if num2 == 0:
        result = "Cannot divide by zero!"
    else:
        result = divide(num1, num2)

else:
    result = "Invalid operation!"

print(f"Result: {result}")
