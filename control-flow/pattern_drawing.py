# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Draw the pattern using while and for loop
while row < size:
    # For loop to print asterisks for each row
    for _ in range(size):
        print("*", end="")
    print()
    row += 1
