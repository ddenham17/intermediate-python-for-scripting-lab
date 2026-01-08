def validate_age(age):
    """
    Validates that the provided age is a positive integer.

    age: The value to validate. It can be a string, float, or integer.

    int: The validated age as an integer if it is a positive whole number.

    error: If the input cannot be converted to an integer, or if the resulting integer is not greater than zero.

    Example:
        To handle the potential error when calling this function, I'm using a try-except block:
        
        try:
            valid_age = validate_age(user_input)
        except ValueError as e:
            print(f"Validation Error: {e}")
    """
    try:
        # Convert to float first to handle cases like "18.0" 
        # then convert to int to ensure it is a whole number
        age_int = int(float(age))
        
        # Check if the number is positive (greater than 0)
        if age_int <= 0:
            raise ValueError(f"Age must be a positive integer!")  
        return age_int
        
    except (ValueError, TypeError):
        # Raise a ValueError when conversion fails
        raise ValueError(f"Input '{age}' is not a valid numerical integer!")

# Example usage:
# print(validate_age(25))    # Returns 25
# print(validate_age(-5))    # Raises ValueError
# print(validate_age("abc")) # Raises ValueError

import math.pi

def calculate_rectangle_area(length, width):
    """Returns area of a rectangle (length * width)."""
    return length * width

def calculate_circle_area(radius):
    """Returns area of a circle (pi * radius^2)."""
    return math.pi * (radius ** 2)

def get_area(shape, *args):
    """
    Calls the correct calculation function based on the shape.
    - For 'rectangle', arguments should be (length, width).
    - For 'circle', arguments should be (radius).
    """
    shape = shape.lower()
    
    if shape == "rectangle":
        # Unpacks two arguments: length and width
        return calculate_rectangle_area(*args)
    elif shape == "circle":
        # Unpacks one argument: radius
        return calculate_circle_area(*args)
    else:
        return "Invalid shape! Please use 'rectangle' or 'circle'."

# Example Usage:
# rect_area = get_area("rectangle", 10, 5)
# circ_area = get_area("circle", 7)
