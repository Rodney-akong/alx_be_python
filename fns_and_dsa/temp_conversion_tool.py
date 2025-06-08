'''
This script will define functions to convert t
emperatures between Celsius and Fahrenheit, 
demonstrating the use of global variables to store 
conversion factors that are accessible within functions.
'''
# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
CELSIUS_OFFSET = 32

def convert_to_celsius(fahrenheit):
    return (fahrenheit - CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_OFFSET

def implement_conversion(temperature, unit):
    try:
        temperature = float(temperature)
        if unit == "C":
            converted_temperature = convert_to_fahrenheit(temperature)
            return f"{temperature}°C is {converted_temperature}°F"
        elif unit == "F":
            converted_temperature = convert_to_celsius(temperature)
            return f"{temperature}°F is {converted_temperature}°C"
        else:
            return "Invalid unit. Please enter C for Celsius or F for Fahrenheit."
    except ValueError:
        return "Invalid temperature. Please enter a numeric value."

def main():
    while True:
        print("Temperature Conversion Tool")
        print("1. Convert temperature")
        print("2. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            temperature = input("Enter the temperature to convert: ")
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            result = implement_conversion(temperature, unit)
            print(result)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
