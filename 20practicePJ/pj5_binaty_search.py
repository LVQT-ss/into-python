def binary_search(lst, element):
    start = 0
    end = len(lst) - 1
    steps = 0

    while start <= end:
        print("Step", steps, ':', str(lst[start:end + 1]))
        steps = steps + 1
        middle = (start + end) // 2
        if element == lst[middle]:
            return middle
        if element < lst[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 3
result = binary_search(mylist, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")
