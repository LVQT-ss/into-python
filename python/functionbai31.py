# biến locals and global 
def say_slogan():
    kteam = 'howkteam'
    print('we are ', kteam)

say_slogan()


lst = ['howkteam',1,2]
def change(parameter):
    parameter[1]='new value '
    print('change successfully ')

print(lst)
change(lst)
print(lst)

# biến global tạo ra biến toàn cục  để tái sử dụng lại hoặc khởi tạo chương trình 

def make_slogan():
    global kteam 
    kteam= 'how kteam'

make_slogan()
print(kteam)


# gloval vs locals 

def make_globa():
    global x 
    x =1 
def local():
    x=5
    print('x in local',x)

make_globa()
print(x)
local()
print(x)
