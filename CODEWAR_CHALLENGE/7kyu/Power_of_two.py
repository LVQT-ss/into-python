def power_of_two(x):
    # Khởi tạo biến exponent với giá trị ban đầu là 0
    exponent = 0 
    
    # Bắt đầu một vòng lặp vô hạn
    while True:
        # Kiểm tra nếu 2 mũ exponent lớn hơn x
        if 2 ** exponent > x:
            # Nếu điều này đúng, trả về False vì x không phải là lũy thừa của 2
            return False
        
        # Kiểm tra nếu 2 mũ exponent bằng x
        if 2 ** exponent == x:
            # Nếu điều này đúng, trả về True vì x là lũy thừa của 2
            return True
        
        # Tăng giá trị của biến exponent lên 1 để kiểm tra lũy thừa tiếp theo
        exponent += 1

# 