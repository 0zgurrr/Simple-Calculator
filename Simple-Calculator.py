def add(a, b):
    return a + b
 
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def calculator():
    print("=== Professional Python Calculator ===")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Exit")

    while True:
        choice = input("Select an operation (1-7): ")

        if choice == '7':
            print("Calculator closing. Goodbye!")
            break

        if choice not in ['1','2','3','4','5','6']:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Please enter a valid number!")
            continue

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {power(num1, num2)}")
        elif choice == '6':
            print(f"Result: {modulus(num1, num2)}")

        print("\n-------------------------\n")

if __name__ == "__main__":
    calculator()

