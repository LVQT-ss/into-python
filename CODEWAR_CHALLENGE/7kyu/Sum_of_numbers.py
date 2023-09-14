def get_sum(a, b):
    # Kiểm tra nếu a và b bằng nhau, trả về a hoặc b (bất kỳ số nào cũng được).
    if a == b:
        return a

    # Xác định số nhỏ và số lớn bằng cách sắp xếp a và b.
    small, big = sorted([a, b])

    # Tạo một danh sách chứa các số nguyên từ small đến big + 1 bằng list comprehension.
    numbers = [i for i in range(small, big + 1)]

    # Tính tổng của các số trong danh sách và trả về kết quả.
    return sum(numbers)

# https://www.codewars.com/kata/55f2b110f61eb01779000053/solutions/python