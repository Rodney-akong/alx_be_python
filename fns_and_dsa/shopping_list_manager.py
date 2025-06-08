'''
Create a Python script named shopping_list_manager.py
 that implements a simple interface for managing a shopping list. 
 This task focuses on using lists to store and manipulate data dynamically.
 Author: Akong Rodney
 Date:08/06/2025
'''

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item = input("Enter the item add: ")
            shopping_list.append(add_item)

        elif choice == '2':
            # Prompt for and remove an item
            item_remove = input("Enter the item to remove ")
            if item_remove in shopping_list:
                shopping_list.remove(item_remove)

        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
