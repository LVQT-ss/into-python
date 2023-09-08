def grow(arr):
    # Khởi tạo biến product với giá trị ban đầu là 1.
    product = 1
    
    # Duyệt qua từng phần tử (number) trong danh sách arr.
    for number in arr:
        # Tích các phần tử trong danh sách bằng cách nhân các số lại với nhau.
        product *= number
    
    # Trả về giá trị tích cuối cùng của các phần tử trong danh sách.
    return product

# https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python