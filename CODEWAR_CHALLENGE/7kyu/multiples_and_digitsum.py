def procedure(i):
    # Tạo danh sách chứa tất cả các bội số của 'i' trong khoảng từ 'i' đến 100
    multiples = list(range(i, 101, i))
    
    # Chuyển mỗi số trong danh sách thành chuỗi để xử lý từng chữ số
    multiples_string = [str(n) for n in multiples]
    
    # Khởi tạo danh sách để lưu tổng các chữ số của từng số
    digit_sums = []
    
    # Duyệt qua từng số trong danh sách các số dưới dạng chuỗi
    for number_string in multiples_string:
        # In giá trị số đang xử lý (chuỗi)
        print(number_string)
        
        # Tính tổng các chữ số trong số và chuyển chúng thành số nguyên
        digit_sum = sum([int(d) for d in number_string])
        
        # Thêm tổng các chữ số vào danh sách 'digit_sums'
        digit_sums.append(digit_sum)
        
    # Trả về tổng của tất cả các tổng các chữ số
    return sum(digit_sums)


print(procedure(2))


def procedure(n):
    return sum(int(d) for i in range(n, 101, n) for d in str(i))