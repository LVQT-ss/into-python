def count_positives_sum_negatives(arr):
    # Kiểm tra xem danh sách 'arr' có rỗng không.
    if len(arr) == 0:
        # Nếu danh sách rỗng, trả về danh sách rỗng.
        return []
    
    # Khởi tạo biến 'positives_cont' để đếm số lượng số dương trong danh sách.
    # Khởi tạo biến 'negatives_sum' để tính tổng của tất cả các số âm trong danh sách.
    positives_cont = sum([1 for i in arr if i > 0 ])
    negatives_sum = sum([i for i in arr if i < 0 ])
    
    # Trả về danh sách gồm số lượng số dương và tổng của tất cả các số âm.
    return [positives_cont, negatives_sum]

# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python


