length = 3 
iter_ = (x for x in range(length))
c = 0 
while c < length:
     print(next(iter_))
     c+=1


length = 3 
iter_ = (x for x in range(length))
c = 0 

while 1:
     try:
          print(next(iter_))
     except StopIteration:
          break

i = ( x for x in range(3))
for value in i:
     print('->',value)

howketeam = {'name':'quocthinh','age':20}
list_values = list(howketeam.items())
print(list_values)
print(list_values[0])
print(list_values[1])

for key,value in howketeam.items():
     print(key, '=>',value)

s = 'how kteam'
for ch in s:
     if ch ==' ':
          continue
     else:
          print(ch)

print('-----------------------------')

for k in (1,2,3):
     print(k)
     if(k%2==0):
          break
else:
     print('done')

print('in ra so le' )
     
for n in (1,2,3):
     if(n%2==0):
          continue
     print(n)
else:
     print('done')

# bài tập 

# bài 1 

# bài 2 
set_ = {5, 8, 1, 9, 4}
sum_of_set = 0 
for value in set_ : 
     sum_of_set += value 
print(sum_of_set)

print('in ra tam giác vuông cân ')
for i in range(1,5):
     s='*'*i
     print(s)

print('in ra một tam giác cân ')

n = 5 
for i in range(1,n):
     s = n -i 
     k = s* " "
     print(k, end='')
     print(((2*i) -1 )*'*')

print('in ra hình bàn cờ ')

n = 9 
print('+', end='')
print((n-1)*'-',end='')
print('+')

for i in range(1,n):
     print('|', end='')
     for j in range(1,n):
          if i%2 ==j%2:
               print(' ', end='')
          else:
               print('#',end='')
     print('|')

print('+', end='')
print((n-1)*'-',end='')
print('+')