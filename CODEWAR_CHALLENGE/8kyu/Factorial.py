def factorial(n):
    output = 1  # Initialize the output variable to 1

    # Check if n is outside the valid range (below 0 or above 12)
    if n > 12 or n < 0:
        raise ValueError  # Raise a ValueError if n is out of range
    else:
        # Calculate the factorial using a for loop
        for x in range(1, n+1):
            output *= x  # Multiply output by each integer from 1 to n
        return output  # Return the calculated factorial value

# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python
# n! = n*(n -1) * 2 * 1 
f = 1 
for i in range(1,3):
    f *= i +1 

print(f)