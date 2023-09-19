def get_decimal(n): 
    # Chuyển số n thành chuỗi và tách nó thành danh sách dựa trên dấu chấm
    n_parts = str(n).split('.')
    
    # Kiểm tra xem danh sách n_parts có chứa phần thập phân hay không
    if len(n_parts) == 1:
        # Nếu không có phần thập phân, trả về 0
        return 0
    
    # Nếu có phần thập phân, nối chuỗi '0.' với phần thập phân và chuyển thành số thực
    return float('0.' + n_parts[1])

# Ví dụ sử dụng hàm get_decimal

result1 = get_decimal(3.14159)
print(result1)  # Kết quả sẽ là 0.14159

result2 = get_decimal(42)
print(result2)  # Kết quả sẽ là 0 (vì không có phần thập phân)

result3 = get_decimal(7.0)
print(result3)  # Kết quả sẽ là 0 (vì không có phần thập phân)

result4 = get_decimal(-123.456)
print(result4)  # Kết quả sẽ là 0.456 (lấy giá trị thập phân dương)

# https://www.codewars.com/kata/586e4c61aa0428f04e000069/solutions/python