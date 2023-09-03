k = range(5)
print(type(k))
print(k)
print(k[1])

print(list(range(2,5)))
print(list(range(4,1,-1)))
print(list(range(2,-3,-1)))

i = ( x for x in range(2,5))
for value in i:
     print('->',value)

# kiểm tra số có ở trong range không 

k = range(99999999999)
print(999999999 in k )

lst = [5,(1,2,3),{'abc','xyz'}]
for i in range(len(lst)):
     print(lst[i])
     i+=1

lst= [1,2,3]
for value in range(len(lst)):
     lst[value] += 1 
print(lst)        

# comprehension 
u =['--'.join((a.capitalize(),b.upper() +c.lower())) for a,b,c in [('name','age','year'),('thinh','20','2003')]]
print(u)
# tương đương vơi1 
n = []
for a,b,c in [('name','age','year'),('thinh','20','2003')]:
     a = a.capitalize()
     b = b.upper()
     c=c.lower()
     n.append('--'.join((a,b + c ) ))
print(n)

# value là số lẻ mới được đưa vào danh sách 
o = {key:value + 1  for key,value in  (('Kteam', 69), ('Tèo', 50), ('Tũn', 14), ('Free Education', 93))
     if value % 2 !=0 }
print(o)


student_list= ['Long', 'Trung', 'Giàu', 'Thành']
#for student in student_list:
     #print(student)
gen = enumerate(student_list)
print(list(gen))

# BÀI TẬP 
# CÂU 1 
lst = [[1,2,3],[4,5,6]]
for value_lst in range(len(lst)):
     print(lst(value_lst))
