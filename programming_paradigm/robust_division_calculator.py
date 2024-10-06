def safe_divide(numerator, denominator):  
    try:
        # Attempt to convert numerator and denominator to float
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division and handle ZeroDivisionError
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
