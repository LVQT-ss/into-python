# 
def inc(x): return x +1

kteam = [1,2,3,4]

print(list(map(inc,kteam)))
# dùng lambda 
print(list(map(lambda x : x + 1, kteam )))
 # dùng lambda 
inc = lambda x: x + 1 
print([inc(x) for x in kteam])

# dùng toold map 
func = lambda x, y: x + y
kteam_1 = [1, 2, 3, 4]
kteam_2 = [5, 6, 7, 8]
kteam = map(func, kteam_1, kteam_2)
print(list(kteam))
# hàm filter 
func = lambda x : x > 0 
kteam = [ 1 ,-3,5, 0 , 2 ,6 , -3 ,-9 ]
print(list(filter(func,kteam)))
print(list(filter(None,kteam)))
print(' comprehension tương ứng ' ) 
print([x for x in kteam if x > 0  ])
# hàm reduce 
print('sử dụng hàm reduce ')
from functools import reduce 
kteam_add = lambda x, y: x + y
kteam = [1, 2, 3, 4, 5]
print(reduce(kteam_add, kteam)) # ((((1+2)+3)+4)+5)

from functools import reduce 
kteam_add = lambda x, y: x * y
kteam = [1, 2, 3, 4, 5]
print(reduce(kteam_add, kteam))

from functools import reduce 

kteam = [1, 2, 3, 4]
kteam_add = lambda x , y : x + y 
kteam_multi = lambda x ,y : x * y 
print(reduce(kteam_add, kteam,10)) 
print(reduce(kteam_multi, kteam,10)) 