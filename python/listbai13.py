# đếm số lần suất hiện của 1 phần tử  trong list 
a = [1,2,3,4,5,6,7,8]
b = a.count(1)
print(b)
# index trả về vị trí của phần tử nằm trong list 
c = a.index(3)
print(c)
# append thêm phần tử vào torng list  
a.append(4)

print(a)
# extend có thể thêm nhiều phần tử vào trong list 
a.extend([5,6])
# phương thức insert thêm phần tử tại vị trí y 
a.insert(0,'leviet')
print(a)
# pop lấy phần tử của y trong list ra ngoài 
m = a.pop(1)
print(m)

# copy - tạo ra 1 bản sao khác nhau không trỏ vào bản gốc 
d= a.copy()
d[0]='thinh'
print(d)
print(a)
# clear xóa các phần tử trong list 
f= a.clear()
print(f)

