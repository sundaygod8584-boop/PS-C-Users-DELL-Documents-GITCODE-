# Simple Calculator

print("===== SIMPLE CALCULATOR =====")

# Numbers
num1 = 7
num2 = 5

# Addition
addition = num1 + num2

# Subtraction
subtraction = num1 - num2

# Multiplication
multiplication = num1 * num2

# Division
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Display results
print("\n===== RESULTS =====")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)