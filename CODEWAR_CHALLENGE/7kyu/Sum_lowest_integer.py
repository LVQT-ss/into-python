def sum_two_smallest_numbers(numbers):
    num = sorted(numbers)
    return num[0] + num[1]

print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))