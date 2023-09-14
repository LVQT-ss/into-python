def special_number(number):
    # Define a list of special numbers
    special_numbers = [0, 1, 2, 3, 4, 5]

    # Convert the input number into a list of its digits
    digits = [int(d) for d in str(number)]

    # Iterate through the digits of the input number
    for digit in digits:
        # Check if the digit is not in the list of special numbers
        if digit not in special_numbers:
            return "NOT!!"  # Return "NOT!!" if a non-special digit is found

    # If all digits are special, return "Special!!"
    return "Special!!"

# https://www.codewars.com/kata/5a55f04be6be383a50000187/train/python