a = int(input("nhập vào lương tháng này : \n"))
b = int(input("nhập vào lương tháng này : \n"))
c = int(input("nhập vào lương tháng này : \n"))

list=[a,b,c]
list.sort()
print(list)


if a > b :
    a, b = b,a 
if a > c: 
    a ,c = c ,a 
if b > c : 
    b,c = c,b
print(a,b,c)