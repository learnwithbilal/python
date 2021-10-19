import sys
from functions import *
operation = input("Enter The Operation: ")

try:
    number01 = int(input("Enter First Number: "))
    number02 = int(input("Enter Second Number: "))
except ValueError:
    print("Error: Not Valid")
    sys.exit(1)

try:

    if operation == "+":
        print(sum(number01, number02))
    elif operation == "-":
        print(sub(number01, number02))
    elif operation == "*":
        print(multi(number01, number02))
    elif operation == "/":
        print(div(number01, number02))
    else:
        print("Try Again")

except ZeroDivisionError:
    print("Can't Division by 0")
