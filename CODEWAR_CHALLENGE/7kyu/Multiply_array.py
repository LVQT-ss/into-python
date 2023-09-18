# Định nghĩa một hàm gọi là multiply_all nhận một danh sách lst làm đối số
def multiply_all(lst):
    # Định nghĩa một hàm lồng nhau gọi là inner nhận một đối số duy nhất n
    def inner(n):
        # Trả về một danh sách bằng biểu đạt danh sách (list comprehension) nhân từng phần tử i trong lst với n
        return [i * n for i in lst]
    
    # Trả về hàm inner (một closure) mà có thể được sử dụng để nhân danh sách với một số cụ thể
    return inner

# Ví dụ sử dụng của hàm multiply_all:

# Định nghĩa một danh sách các số
numbers = [1, 2, 3, 4, 5]

# Tạo một hàm gọi là multiply_by_2 để nhân tất cả các phần tử trong danh sách với một số cụ thể (2 trong trường hợp này)
multiply_by_2 = multiply_all(numbers)

# Sử dụng hàm multiply_by_2 để nhân danh sách với số 2
result = multiply_by_2(2)

# In kết quả
print(result)  # Kết quả: [2, 4, 6, 8, 10]
