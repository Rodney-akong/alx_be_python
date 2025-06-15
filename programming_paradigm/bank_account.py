'''
two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, 
which interfaces with the class through command line arguments to perform banking operations.
Author: Akong Rodney
Date: 15/06/2025
'''
class BankAccount:
    def __init__(self, initial_balance = 0):
        self.__account_balance = initial_balance
    def deposit(self, amount):
        self.__account_balance += amount
    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False 

    def display_balance(self):
        print(f"Current balance: ${self.__account_balance:.2f}")


account = BankAccount()
print("Initial balance:")
account.display_balance()
