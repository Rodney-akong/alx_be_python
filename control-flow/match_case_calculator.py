'''
Develop a Python script named match_case_calculator.py. 
This calculator will prompt the user to enter two numbers and
select an operation (addition, subtraction, multiplication, or division).
The script will then perform the selected operation using a Match Case statement and display the result.
'''

#Get the first number from the user

num1 = float(input("Enter the first number:"))

# Get tge second number from the user

num2 = float(input("Enter the second number:"))

#Get the operator from the user

operation = input("Choose the operation (+, -, *, /): ")
match operation :
    case "+":
        result = num1 + num2
        print("The result is ", result.)
    case "-":
        result = num1 - num2
         print("The result is ", result.)
    case "*":
        result = num1 * num2
         print("The result is ", result.)
    case "/":
        if num2 != 0:
           result = num1 / num2
            print("The result is ", result.)
        else:
            print("Cannot divide by zero.")
    #case_:
       #print("Cannot divide by zero.")

            
    
 