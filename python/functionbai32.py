# return trong python 
def cal_rec_per(width,height):
    per = (width + height) * 2 
    return per

rec_1_width = 5 
rec_1_height = 3 

rec_1_per = cal_rec_per(rec_1_width,rec_1_height)

print(rec_1_per)

print(cal_rec_per(7,4))

def return_ter_fuction():
    print(' chungta sử dụng return để ngắt hàm ')

    return
    print('ham print này dĩ nhiên không được gọi')

none = return_ter_fuction()
print(type(none))

# tính chu vi và diện tích 
def cal_rec_area_per(width,height):
    per = (width + height) * 2 
    area = width * height
    return per, area 

rec_width= 3 
rec_height = 9 
rec_per , rec_area = cal_rec_area_per(rec_width,rec_height)

print(rec_per,rec_area)

# bai tap 1 

# Khởi tạo danh sách các điểm (mỗi điểm là một tuple gồm x và y)
lst = [(-5, -20),(-4, -15), (-3, 4), (-2, 9), (-1, 7), (0, 1), (1, -7), (2, -9), (4, 81), (5, 130)]

# Khởi tạo danh sách A và B để lưu các điểm thuộc và không thuộc hàm f(x)
lstA = []
lstB = []

# Khởi tạo tổng tung độ của danh sách A và B
tongA = 0
tongB = 0

# Định nghĩa hàm số f(x) theo công thức đã cho
def f(x):
    f = x**3 + 2*x**2 - 4*x + 1
    return f

# Duyệt qua từng điểm trong danh sách lst
for c in lst:
    # Tính giá trị của hàm số f(x) tại điểm x
    f_x = f(c[0])
    
    # So sánh giá trị của f(x) với tung độ y của điểm
    if f_x == c[1]:
        # Nếu giống nhau, điểm thuộc hàm f(x), thêm vào danh sách A và cộng tổng tung độ
        lstA.append((c[0], c[1]))
        tongA += c[1]
    else:
        # Nếu khác nhau, điểm không thuộc hàm f(x), thêm vào danh sách B và cộng tổng tung độ
        lstB.append((c[0], c[1]))
        tongB += c[1]

# Tính giá trị tuyệt đối của hiệu tổng tung độ của danh sách A và B
suby = abs(tongA - tongB)

# In ra các điểm thuộc và không thuộc hàm f(x)
print('Các điểm thuộc hàm f(x) là: ', lstA)
print('Các điểm không thuộc hàm f(x) là: ', lstB)

# In ra giá trị tuyệt đối của hiệu tổng tung độ
print('Giá trị tuyệt đối tổng tung độ là: ', suby)

# bài tạp 2 
a = 32 
b = 59 
c = 8 
d = 24 
e = 15 

f =  2*max(a,b,c,d,e) - 1
print('so lon nhat la : ',f )

