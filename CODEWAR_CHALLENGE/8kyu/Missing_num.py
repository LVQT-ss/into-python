def pipe_fix(nums):
    
    min_num = nums[0]  # Lấy số đầu tiên trong chuỗi (đã sắp xếp từ bé đến lớn)
    max_num = nums[-1]  # Lấy số cuối cùng trong chuỗi (đã sắp xếp từ bé đến lớn)
    
    missing_nums = []  # Tạo một danh sách để lưu trữ các số bị thiếu
    
    for num in range(min_num, max_num + 1):
        missing_nums.append(num)  # Thêm các số từ min_num đến max_num vào danh sách
    
    return missing_nums  # Trả về danh sách các số bị thiếu

# https://www.codewars.com/kata/56b29582461215098d00000f/train/python

def pipe_fix(nums):
    first = nums[0]
    last = nums[-1]
    return list(range(first,last+1))
# code này nhanh hơn 