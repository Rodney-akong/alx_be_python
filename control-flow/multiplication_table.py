'''
Create a Python script named multiplication_table.py
This script will ask the user to enter a number
then use a for loop to print the multiplication table for that number from 1 to 10.
'''
# Take input from the user.

number = int(input("Enter a number to see its multiplication table: "))
#Use a for loop to loop through the range of 10 integers

for i in range(1, 11):

    y = number * i

    print(number, "*", i, "=", y)