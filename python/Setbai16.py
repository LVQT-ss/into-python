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