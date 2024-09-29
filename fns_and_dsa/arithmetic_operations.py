# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on the provided operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform - "add", "subtract", "multiply", or "divide".

    Returns:
        float or str: The result of the arithmetic operation, or a message in case of division by zero.
    """
    # Perform the appropriate arithmetic operation based on the given operation string.
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."  # Return a consistent message for division by zero.
        return num1 / num2  # Perform division if num2 is not zero.
    else:
        return "Invalid operation"  # Return a message if the operation is not recognized.
