def count_by(x, n):
    # Khởi tạo một danh sách để lưu trữ các số kết quả
    result = []
    
    # Duyệt qua các số nguyên từ 1 đến n (bao gồm cả n)
    for i in range(1, n + 1):
        # Tính tích của x và i và thêm vào danh sách kết quả
        result.append(i * x)
    
    # Trả về danh sách kết quả
    return result
# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
