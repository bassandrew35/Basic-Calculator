

def addition():
    print("Enter first number")
    x = input()
    num1 = float(x)
    print("Enter second number")
    y = input()
    num2 = float(y)
    return (num1 + num2)

def subtraction():
    print("Enter number to be subtracted")
    x = input()
    num1 = float(x)
    print("Enter second number")
    y = input()
    num2 = float(y)
    return (num1 - num2)

def multiplication():
    print("Enter first number")
    x = input()
    num1 = float(x)
    print("Enter second number")
    y = input()
    num2 = float(y)
    return (num1 * num2)

def division():
    print("Enter dividend")
    x = input()
    num1 = float(x)
    print("Enter divisor")
    y = input()
    num2 = float(y)
    return (num1 / num2)

optionChoice = ["Addition", "Subtraction", "Multiplication","Division"]
for x in range(2):
    print("Enter number of choice")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    optionNum = input();
    optionNum = int(optionNum)
    print(optionChoice[optionNum - 1], ":")
    if optionNum == 1:
        result = addition()
        print("Answer ---> ", result)
    elif optionNum == 2:
        result = subtraction()
        print("Answer ---> ", result)
    elif optionNum == 3:
        result = multiplication()
        print("Answer ---> ", result)
    elif optionNum == 4:
        result = division()
        print("Answer ---> ", result)
    else:
        print("invalid option")
