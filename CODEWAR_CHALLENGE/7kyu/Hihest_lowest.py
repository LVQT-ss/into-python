def high_and_low(numbers):
    # Split the input string into a list of numbers
    numbers_list = [int(num) for num in numbers.split()]

    # Find the highest and lowest numbers in the list
    low = min(numbers_list)
    high = max(numbers_list)

    # Return their sum
    return high, low

# Test the function with your input
input_string = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
high, low = high_and_low(input_string)
print(f"Highest: {high}, Lowest: {low}")

def high_and_low(numbers):
    # Split the input string into a list of numbers
    numbers_list = [int(num) for num in numbers.split()]

    # Find the highest and lowest numbers in the list
    low = min(numbers_list)
    high = max(numbers_list)

    # Return their sum
    return f'{high} {low}'

