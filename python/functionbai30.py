def kteam(k, t, e,*, r='kter'): 
    print(k)
    print(t, e)
    print('end', r)

lst = ['123', 'kteam', 69.96]

# Convert the elements to the appropriate types
#kteam(lst[0], lst[1], lst[2], lst[3])
kteam(*lst,r='k9')

def a(*, s, d):
    print(s, d)

d = [123, 123]
a(s=d[0], d=d[1])

# a(*('a','b'))
    # trong 1 hàm chỉ dùng 1 packing  

def ex(*args,kter):
    #print(args)
    print(kter)

#ex('kteam',69,'henty')

ex(*(x for x in range(70)),kter=' quoc thinh')


def ktem(name,member):
    print('n',name)
    print('m',member)
dic={'name':'kteam','member':79}

ktem(*dic)

def kte(**kwarfs):
    for key,value in kwarfs.items():
        print(key,'=>',value)

kte={'name':'kteam','member':79} 
