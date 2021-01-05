import math
def add_nums(x, y):
    print(x + y)

def subtract_nums(x, y):
    print(x - y)

def multiply_nums(x, y):
    print(x * y)

def divide_nums(x, y):
    print(x / y)

def power_nums(x, y):
    print(x ** y)

def squareRoot_nums(x):
    print(math.sqrt(x))

usrinp = input("\033[1;32;1mAddition, Subtraction, Multiplication, Division, Power, Square Root\n>>> ")

if usrinp == "Addition":
    num1 = int(input("\033[1;31;1mFirst Number: "))
    num2 = int(input("\033[1;36;1mSecond Number: "))
    print("\033[1;32;1m")
    add_nums(num1, num2)
elif usrinp == "Subtraction":
    num1 = int(input("\033[1;31;1mFirst Number: "))
    num2 = int(input("\033[1;36;1mSecond Number: "))
    print("\033[1;32;1m")
    subtract_nums(num1,num2)
elif usrinp == "Multiplication":
    num1 = int(input("\033[1;31;1mFirst Number: "))
    num2 = int(input("\033[1;36;1mSecond Number: "))
    print("\033[1;32;1m")
    multiply_nums(num1, num2)
elif usrinp == "Division":
    num1 = int(input("\033[1;31;1mFirst Number: "))
    num2 = int(input("\033[1;36;1mSecond Number: "))
    print("\033[1;32;1m")
    divide_nums(num1, num2)
elif usrinp == "Power":
    num1 = int(input("\033[1;31;1mNumber: "))
    num2 = int(input("\033[1;36;1mTo the power of:"))
    print("\033[1;32;1m")
    power_nums(num1,num2)
elif usrinp == "Square Root":
    num1 = int(input("\033[1;33;1mNumber: "))
    print("\033[1;32;1m")
    squareRoot_nums(num1)

print("Thanks For Using JaiCalc")