'''
two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, 
which interfaces with the class through command line arguments to perform banking operations.
Author: Akong Rodney
Date: 15/06/2025
'''
class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
         

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
        return self.account_balance