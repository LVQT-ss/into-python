# list giới hạn bởi cặp ngoặc vuông []
# các phần tử được cách nhau bởi dấu , 
# list có khả năng chứa mọi giá trị của đối tượng python và bao gồm chính nó 
teoName = 'teo'
teoAge = 17 
print(teoName)
print(teoAge)
# các list có thể chứa các list 
a=[1,2,'thinh',[1,2,3]]
b = [i for i in range(3)] # tạo ra 1 list từ 0 - 3
c= [[n,n*1,n*2] for n in range (1,4)]
print(a)
print(b)
print(c)
# tách  từng kĩ tự trong chuỗi 
d = list('kteam')
print(d)

# toán tử,  
f = [1,2]
f += ['one ','two']
g = 2 *f 
print(f)
print(g)