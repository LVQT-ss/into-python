a=0
b=3 
if a > 0 :
    print('a lon hon 0')
elif a == 0:
    print('a bang 0')
else :
    print('a nho hon 0')
if b < 1:
    print('b nho hon 1')
elif b > 1:
    print('b lon hon 1')


print('Số thứ 1 :')
n_1=int(input())
print('số thứ 2 :')
n_2=int(input())
print('số thứ 3 :')
n_3=int(input())

if n_1 > n_2 > n_3:
    print('số lớn nhất là : ' + str(n_1))
elif n_2 > n_1 > n_3:
    print('số lớn nhất là : ' + str(n_2))
else:
    print('số lớn nhất là : ' + str(n_3))