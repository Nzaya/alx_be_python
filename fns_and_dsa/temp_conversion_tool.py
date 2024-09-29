# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    Formula: (Fahrenheit - 32) * (5/9)
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    Formula: (Celsius * (9/5)) + 32
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    """
    Main function to interact with the user, taking input and calling the appropriate conversion function.
    """
    try:
        # Prompt the user to enter the temperature
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # Convert the input to a float for numeric operations

        # Ask if the temperature is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform the appropriate conversion based on user input
        if unit == "C":
            # Convert Celsius to Fahrenheit
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")

        elif unit == "F":
            # Convert Fahrenheit to Celsius
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")

        else:
            # Handle invalid input for the temperature unit
            raise ValueError("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        # Catch any ValueError and display an appropriate message
        print("Invalid temperature. Please enter a numeric value.")

# Run the main function
if __name__ == "__main__":
    main()
