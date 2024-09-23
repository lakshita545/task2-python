
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulo(a,b):
    return a % b

def expo(a,b):
    return a**b

print("**********CALCULATOR**********")
print("Select the operation to be perform.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulo ")
print("6.Exponential ")
print()
while True:
    
    choice = input("Enter your choice : ")

    
    if choice in ('1', '2', '3', '4', '5','6'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choice == '5':
            print(num1, "%", num2, "=", modulo(num1, num2))
        
        elif choice == '6':
            print(num1, "**", num2, "=", expo(num1, num2))
        
    
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          print("**********The End**********")
          break
    else:
        print("Invalid Input")