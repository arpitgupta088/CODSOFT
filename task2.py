# Define functions for basic arithmetic operations +,-,*,/
def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mult(x, y):
  return x * y

def div(x, y):
  if y == 0:
    return "Error: Cannot Divide by zero!"
  return x / y

# From here user can input two numbers with an operation choice
num1 = float(input("Enter the first number you want: "))
num2 = float(input("Enter the second number you want: "))

print("Choose an operation among the following:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice - (1/2/3/4): "))

# Perform the calculation based on the user's choice
if choice == 1:
  result = add(num1, num2)
elif choice == 2:
  result = sub(num1, num2)
elif choice == 3:
  result = mult(num1, num2)
elif choice == 4:
  result = div(num1, num2)
else:
  result = "Error: Invalid operation choice!"

# Display the result
print("Result:", result)