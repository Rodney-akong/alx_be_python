'''
Task Description:

Create a Python script named book_class.py. 
In this script, define a Book class that uses specific magic methods to enhance its functionality. #
This class will model a book with attributes for the title, author, and publication year.
Author: Akong Rodney
Date: 24/06/2025
'''
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(str(book1))
    print(repr(book1))
    del book1
    