def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def exponential(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y > 1:
        return x ** y
    else: 
        return "Second shouldn't be less the 0"

# def modulus(x, y): 
#     if 

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponential")
    print("6. Modulus")
    print("7. Floor Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choice == '5':
            print(num1, "**", num2, "=", exponential(num1, num2))
        
        # elif choice == '6':
        #     print(num1, "%", num2, "=", modulus(num1, num2))

        # elif choice == '7':
        #     result = divide(num1, num2)
        #     print(num1, "//", num2, "=", floorDivision)

    else:
        print("Invalid input")


# Run the calculator
calculator()