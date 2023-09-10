def containsDuplicate(nums):
    # Tạo một tập hợp rỗng để lưu trữ các phần tử duy nhất
    hashset = set()

    # Lặp qua từng phần tử trong danh sách 'nums' đầu vào
    for n in nums:
        # Kiểm tra xem phần tử hiện tại 'n' có trong 'hashset' không
        if n in hashset:
            # Nếu 'n' là một bản sao, trả về True
            return True
        
        # Thêm 'n' vào 'hashset' nếu nó không phải là một bản sao
        hashset.add(n)
    
    # Nếu không tìm thấy bản sao sau khi lặp qua toàn bộ danh sách, trả về False
    return False

# https://leetcode.com/problems/contains-duplicate/