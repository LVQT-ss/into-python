def add(num1, num2):
    # Chuyển đổi num1 và num2 thành chuỗi để có thể thao tác từng chữ số.
    num1 = str(num1)
    num2 = str(num2)
    
    # Tìm độ dài lớn nhất giữa num1 và num2 để xác định độ dài tối đa cho kết quả.
    largest_length = max(len(num1), len(num2))
    
    # Đảm bảo cả num1 và num2 có cùng độ dài bằng cách thêm các chữ số '0' vào đầu chuỗi.
    num1 = num1.rjust(largest_length, '0')
    num2 = num2.rjust(largest_length, '0')
    
    # Khởi tạo danh sách "totals" để lưu kết quả phép cộng từ hàng đơn vị đến hàng cao nhất.
    totals = [int(d1) + int(d2) for d1, d2 in zip(num1, num2)]
    
    # Chuyển danh sách "totals" thành một chuỗi số nguyên và trả về kết quả.
    return int(''.join([str(total) for total in totals]))


# https://www.codewars.com/kata/5effa412233ac3002a9e471d/solutions/python