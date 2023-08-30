# được giới hạn bởi cặp ()
# các phần tử của tuple được phân cách nhau bởi dấu , 
# tuple có khả năng chứa mọi giá trị 
# tốc độ truy xuất của tuple nhanh hơn list 
# dung lượng chiếm bộ nhớ nhỏ hơn list 
# bảo vệ dữ liệu của bạn  sẽ không bị thay đổi 
# có hte63 dùng lạm key của dictionary 

# tuple không có khái niệm comprehension 
# muốn sử dụng comprehension trong tuple thì phải qua  1 bước trung gian (generator expression)
tup = (i for i in range(10) if i %2 == 0)
a = tuple(tup)
print(a)

tuple = (1,2,3)
print(tuple[1])
print(len(tuple))
# list có thể thay đổi được các phần tử trong list nhưng với tuple thì không 
# để thay đổi giá trị bên trong tuple thì chúng ta có thể biến 1 list trong tuple nên khi đó chúng ta có thể thay đổi được giá trị 
c = tuple.count(1)
print(c)
d = tuple.index(3)
print(d)