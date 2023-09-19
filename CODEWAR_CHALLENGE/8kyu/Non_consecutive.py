def first_non_consecutive(arr):
    if len(arr) <= 1:
        return None  # Handle empty or single-element arrays

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]

    return None  # Return None if the array is consecutive

# Test cases
print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))  # Output: 6
print(first_non_consecutive([1, 2, 3, 4, 5, 6, 7]))  # Output: None
print(first_non_consecutive([]))  # Output: None
print(first_non_consecutive([42]))  # Output: None
