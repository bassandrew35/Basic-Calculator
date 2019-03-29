

def addition():
    print("Enter first number")
    x = input()
    num1 = int(x)
    print("Enter second number")
    y = input()
    num2 = int(y)
    return (num1 + num2)

def subtraction():
    print("Enter first number")
    x = input()
    num1 = int(x)
    print("Enter second number")
    y = input()
    num2 = int(y)
    return (num1 - num2)

def multiplication():
    print("Enter first number")
    x = input()
    num1 = int(x)
    print("Enter second number")
    y = input()
    num2 = int(y)
    return (num1 * num2)

def division():
    print("Enter first number")
    x = input()
    num1 = int(x)
    print("Enter second number")
    y = input()
    num2 = int(y)
    return (num1 / num2)

for x in range(2):
    print("Enter number of choice")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    option = input();
    print(option)
    if option == "1":
        result = addition()
        print(result)
    elif option == "2":
        result = subtraction()
        print(result)
    elif option == "3":
        result = multiplication()
        print(result)
    elif option == "4":
        result = division()
        print(result)
    else:
        print("invalid option")
