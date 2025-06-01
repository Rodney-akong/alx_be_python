'''
Develop a Python script named pattern_drawing.py. This script will prompt the user 
to enter a positive integer, 
then use nested loops to print a square pattern of that size made of asterisks (*).
Author: Akong Rodney
Date: 01/06/2025
'''

size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    for col in range(size):
        print("*", end = "")
    print()
    row +=1