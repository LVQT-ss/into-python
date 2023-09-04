# positional argument để đâu thì gán vào đó  
# keyword argument đặt biến vào trong và gán thằng nào thì thằng đó vào phần  a hoặc b 
def kteam(a,b):
    pass
kteam(3,'free education') # positional argument đi trước keyword nếu gán cả 2 argument vào cùng 1 chỗ 
kteam(a=3,b='free education') # keyword argument 

print(sorted([3,4,1],reverse=True))

# vấn đề 
def Teo(a,b=2,c=3,d=4):
    f = (a+d) *(b+c)
    print(f)
Teo(1,d=5)
# kết hợp pos và key
def kteam(pos,*,key,key2):
    print(pos)
    print(key)
    print(key2)

kteam(1,key=2,key2='quocthin')

# nếu cho default value thì truyền vào 1 giá trị là được 
def kteam(pos,*,key=1,key2=2):
    print(pos)
    print(key)
    print(key2)

kteam(1)


# bài tập 
#sorted(iterable, /, *, key=None, reverse=False)
# các positional only là iterable còn các keyword only là key và reverse 
