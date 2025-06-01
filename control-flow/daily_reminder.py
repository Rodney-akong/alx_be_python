'''
Develop a script named daily_reminder.py. 
This script will ask the user for a single 
task, its priority level, and if it is time-sensitive. 
The program will then provide a customized reminder for that task, 
demonstrating control flow and loops without relying on data structures 
to store multiple tasks.

Author: Akong Rodney
Date:01/06/2025
'''

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound.lower() == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Please complete it as soon as possible."
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound.lower() == "yes":
            reminder += " that requires attention today!"
        else:
            reminder += ". Try to complete it within a few days."
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound.lower() == "yes":
            reminder += " that requires attention today!"
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level."

print("Reminder:", reminder)
