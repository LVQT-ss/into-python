def automorphic(n):
    # Calculate the square of the input number and convert it to a string
    squared = str(n ** 2)

    # Convert the input number to a string
    n = str(n)

    # Calculate the length of the input number as a string
    n_length = len(n)

    # Check if the last n_length digits of the squared number match the input number
    if squared[-n_length:] == n:
        return "Automorphic"  # If they match, return "Automorphic"

    # If they don't match, return "Not!!"
    return "Not!!"

# https://www.codewars.com/kata/5a58d889880385c2f40000aa/train/python