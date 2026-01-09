import random
import string

def create_password(length):
    """
    Creates a random password of a specific length.
    
    length (int): Desired length of the password (must be > 8).
        
    str: A randomly generated alphanumeric password.
    """
    # Validate the input length is an integer greater than 8
    if not isinstance(length, int) or length <= 8:
        return "Error! Password length must be an integer greater than 8."

    # Define the character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    
    # Combine pools for full randomness
    all_characters = lower + upper + digits
    
    # Create the password
    # random.choices picks a number of random characters from the pool based on the entered length
    password = ''.join(random.choices(all_characters, k=length))
    
    return password

# Example Usage:
# length = int(input("Enter desired password length: "))
# print(f"Your new password is: {create_password(length)}")

from datetime import datetime

def calculate_days_between(date_str1, date_str2):
    """
    Takes two date strings in 'YYYY-MM-DD' format 
    and returns the absolute difference in days.
    """
    # Define the expected format
    date_format = "%Y-%m-%d"
    
    try:
        # Convert strings into datetime objects
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        
        # Subtract the dates to get the difference
        difference = date2 - date1
        
        # Use abs() to ensure the result is a positive number regardless of order
        return abs(difference.days)
        
    except ValueError:
        return "Invalid date format! Please use 'YYYY-MM-DD'."

# Example Usage:
# first_date = input("Enter first date 'YYYY-MM-DD': ")
# second_date = input("Enter second date 'YYYY-MM-DD': ")
# result = calculate_days_between(first_date, second_date)
# print(f"The difference is {result} days.")

import math

def calculate_circle_area(radius):
    """
    Calculates the area of a circle given the radius entered.
    
    radius (float): The radius of the circle.

    float: The calculated area of the circle.
    """
    # Imported math.pi module to use a precise value of pi to calculate with
    area = math.pi * (radius ** 2)
    return area

# Example Usage:
# r = float(input("Enter the radius of the circle: "))
# print(f"The area of the circle is: {calculate_circle_area(r)}")
# r = 7, area = pi * 7^2. area = 153.93804002589985
