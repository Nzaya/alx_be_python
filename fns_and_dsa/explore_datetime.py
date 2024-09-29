from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(current_date):
    # Prompt the user for the number of days to add
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    
    # Calculate the future date
    future_date = current_date + timedelta(days=number_of_days)
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

# Main function to run the script
def main():
    # Display the current date and time
    current_date = display_current_datetime()
    
    # Calculate and display the future date
    calculate_future_date(current_date)

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()
