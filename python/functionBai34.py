# thay vì sử dụng để khai hàm dùng từ khóa def thì chúng ta có thể sử dụng lamda ( hàm nặc danh ) viết hàm trong hàm nhanh chóng 
# lamda là 1 expesstion không phải 1 câu lệnh | lamda không cần dùng lệnh if và return 

def eva(a,b,c):
    return (a +b +c )/3

print(eva(1,2,3))

# dùng lambda 

ave = lambda a,b,c: ( a+b+c)/3 
print(ave(1,3,2))

# default argument 
x_power_a = lambda x , a = 2:x ** a 

print(x_power_a(2,5))

# phân biệt global và locals 

def kteam():
    mem = lambda x : x + ' is a member of kteam'
    return mem 
call_mem = kteam()
print(call_mem('long'))
print(call_mem)


# vì sao sử dụng lambda: sử dụng những hàm có cấu trúc đơn giản không có nhiều cấu trúc như def 
# sử lý ma trận cực kì dễ để ứng dụng trong machine learning , xử lý ảnh 

kteam_lst = [lambda x : x ** 2 , lambda x : x**3 , lambda x : x ** 4 ]
print(kteam_lst[-1](3))

kteam_lst = [lambda x : x ** 2 , lambda x : x**3 , lambda x : x ** 4 ]
for func in kteam_lst :  
    print(func(3))

find_greater = lambda x, y : x if x > y else y 
print(find_greater(1,3))  

def kteam(first):
    return lambda second: first + second
slogan = kteam('how kteam')
print(slogan('free education'))