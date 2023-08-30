# dict là 1 cặp key:  value
dic = { 'name' :  'quoc thinh', 'member ': 69 }
print(dic)
print(type(dic))
# khởi tạo 1 dist rỗng  thì không bỏ gì vào dic {}
# sử dụng comprehension 
dic_1 = { key: value for key,value in [('name','thinh' ),('member', 69)]}
print(dic_1)

class Map_class:
    def keys(self):
        return[1,2,3]
    def __getitem__(self,key):
        return key*2
map_obj=Map_class()
dic = dict(map_obj)
print(dic)

# contrucstor 
iter_ = [('name', 'Kteam'), ('member', 69)]
dic = dict(iter_)
print(dic)
print(type(dic))




f = [('ac'),('ce')]

print(dict(f))
# khởi tạo bằng keyword 
my_name = ' spaceX '
age = 21
dic_2 = dict(my_name=' thinh ' , age =20)
print(dic_2)
print(my_name)

# khởi tạo fromkeys 
iter_ = ('name','number')
dic_none = dict.fromkeys(iter_,'thinhle')
print(dic_none)
# lấy giá trị ra 
print(dic['name'])

# cách cộng giá trị trong dic 
dic_3 = dict(t=69,tl='thinhle')
dic_3['t'] = dic_3['t'] +1 
dic_3['tl']=dic_3['tl'] + 'vietquoc'
print(dic_3)