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
# toán tử is kiểm tra hai biến có cùng trỏ đến cùng 1 đối tượng hay không 
k = [1,2,3]
e = [1,2,3] 
print(k is e) 

# kiểm tra trong list ( in ) và lấy phần tử từ list 
h = [1,2,3,4,5,6,7,8]
print(1 in h )
print(h[0])
print(h[1:6])
print(h[:3])
print(h[2:])
# thay đổi phần tử của list 
m = ['le','viet','quoc','thinh']
m[0] = 'thinh'
n=m[0]
print(n)
print(m)
# ma trận 
o = [[1,2,3],[4,5,6],[7,8,9]]
u = list(o)
print(o)
print(u)
u[0] = 'thinh'
print(o)
print(u)

# truy vấn phần tử trong ma trận 
print(o[0][1])
# không được phép gán list này sang list kia 
# dùng list để gán thay đổi giá trị lúc này giá trị đã được clone ra tạo 1 list mới để thay đổi trong biến 

q = list(k)
print(q)
print(k)
q[0]='thinh '
print(q)
print(k)
# bài tập 
s = 'aaaaaaaAAAAAaaa//123123//000000//&&TTT%%abcxyznontqfadf'
p=s.strip('abcxyznontqfadfA/1230&%')
print(p)