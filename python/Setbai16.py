# set không chứ phần tử trùng lặp 
# set không phải là 1 hasable object 
# set không lưu được kiểu dữ liệu list 
# set không chứa đc hashable type 

set_1 = {69,69,69}
print(set_1)
print(type(set_1))

set_2 = {' quoc thing ', 1, 2, 3 , (1,2,3)}
print (set_2)

set_3= { value for value in range(3)}
print(set_3)

set_4=set('le viet quoc thinh')
print(set_4)

# toán tử 
print((1,2) in {(1,2),3})

# toán tử trừ 
print({1,2,3} - {2,3})
# lấy ra 2 toán tử trung nhau trong set 
print({1,2,3} & {1})

print({1,2,3} | {5})
# lấy tất cả nhưng không lấy những phần tử trùng nhau 
print({1,2,3} ^ {1,4})

print(set_2.pop())
# phương thức remove và discard ( nên dùng discard vì không thông báo lỗi khi xóa đi 1 phần tử ở bên trong set )
 
set_6 = {5,6,7}
set_6.add(4)
print(set_6)