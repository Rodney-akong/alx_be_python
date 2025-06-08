'''
In this script, define a function that performs basic arithmetic operations.
Author:Akong Rodney
Date:08/06/2025
'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

add = "+"
subtract = "-"
multiply = "*"
divide = "/"

def perform_operation(num1,num2,operation):
    if operation == add:
        add_new = num1 + num2
        print(add_new)

    elif operation == subtract:
        subtract_new = num1 - num2
        print(subtract_new)

    elif operation == multiple:
        multiple_new = num1 * num2
        print(multiple_new)

    elif operation == divide:
        if num2 == 0:
            print("Value cannot be divided by 0")
        else:
            divide_new = num1 / num2
            print(divide)

perform_operation(num1,num2,perform_operation) 


