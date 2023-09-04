# yeild gần giống return thay vì trả object thì trả về 1 generator 

kteam_lst = [1,'kteam', 2 ]

for value in kteam_lst:
    print(value)

def square(lst):
   for num in lst:
       yield num **2

kteam_ret = square([1,2,3])
for value in kteam_ret: 
    print(value)

def gen():
    for value in range(3):
        print('yield',value + 1 , 'times')
        yield value 

for value in gen():
    print(value) 

def gen():
    yield 'kteam'
    print('this is the second yield')
    yield 'kteam'
    print('this is the last yield')
    yield 'kteam'
    print('will not return anything')

for value in gen():
    print(value)

def ga():
    while True:
        x = yield
        yield x **2 
g = ga()
next(g)
print(g.send(2))
next(g)
print(g.send(10))


      