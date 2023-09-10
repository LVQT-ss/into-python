def pre_fizz(n):
    result = []  # Create an empty list to store the numbers
    for i in range(1, n + 1):
        result.append(i)  # Add each number to the list
    return result  # Return the list of numbers

# Example usage:
n = 5  # Change n to the desired value
print(pre_fizz(n))
