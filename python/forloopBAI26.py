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

