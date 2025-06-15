'''
two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, 
which interfaces with the class through command line arguments to perform banking operations.
Author: Akong Rodney
Date: 15/06/2025
'''
class BankAccount:
    def __init__(self, account_balance = 0):
        self.__account_balance = account_balance
    def deposit(self, amount_1):
        self.__account_balance += amount_1
    def withdraw(self, amount_1):
        if amount_1 <= self.__account_balance:
            self.__account_balance -= amount_1
            return True
        else:
            return False 

    def display_balance(self):
        print(f"Current balance: ${self.__account_balance:.2f}")


'''add = BankAccount(0)
add.deposit(0)
print(add.display_balance())'''