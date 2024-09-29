# Function to display the menu options
def display_menu():
    # Ensure the text "Shopping List Manager" is printed exactly as expected
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main function to manage the shopping list
def main():
    # Start with an empty shopping list
    shopping_list = []

    # Loop until the user decides to exit
    while True:
        display_menu()  # Display the menu at the beginning of each loop iteration
        try:
            # Ensure the input is a number by casting it to an integer
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        # Add item to the shopping list
        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item cannot be empty. Please try again.")

        # Remove item from the shopping list
        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        # View the current shopping list
        elif choice == 3:
            if shopping_list:
                print("\nCurrent Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is currently empty.")

        # Exit the program
        elif choice == 4:
            print("Goodbye!")
            break

        # Handle invalid menu choices
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Check if the script is being run directly
if __name__ == "__main__":
    main()
