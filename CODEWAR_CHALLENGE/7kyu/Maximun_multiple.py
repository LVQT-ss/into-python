def max_multiple(divisor, bound):
    result = divisor  # Khởi tạo biến result bằng giá trị của divisor.

    while True:  # Bắt đầu vòng lặp vô hạn.
        if result > bound:  # Kiểm tra nếu giá trị result vượt quá bound.
            return result - divisor  # Trả về kết quả (số nguyên lớn nhất chia hết cho divisor và không vượt quá bound).
        result += divisor  # Tăng giá trị result lên bằng divisor để kiểm tra số tiếp theo.

# Ví dụ 1:
print(max_multiple(3, 10))  # Kết quả: 9
# Số nguyên lớn nhất chia hết cho 3 và không lớn hơn 10 là 9.

# Ví dụ 2:
print(max_multiple(5, 25))  # Kết quả: 25
# Số nguyên lớn nhất chia hết cho 5 và không lớn hơn 25 là 25.

# Ví dụ 3:
print(max_multiple(7, 20))  # Kết quả: 14
# Số nguyên lớn nhất chia hết cho 7 và không lớn hơn 20 là 14.

# Ví dụ 4:
print(max_multiple(2, 3))   # Kết quả: 2
# Số nguyên lớn nhất chia hết cho 2 và không lớn hơn 3 là 2.
