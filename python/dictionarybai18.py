d = {'thinh':'quoc thinh ',(1,2) :69}
print(d)
d2 = d.copy()
print(d2)
d3=d2.get('thinh','levietquocthinh')
print(d3)
# Trả về một giá trị thuộc lớp dict_items. Các giá trị của dict_items sẽ là một tuple với giá trị thứ nhất là key, giá trị thứ hai là value.
value = list(d.items())
print(value[0])
# pop xóa 1 parameter 
f = d.pop('thinh') # có popitem
print(d)
# thêm giá trị vào dictionary - setdefault
g = d.setdefault('leviet','quocthinh')
print(g)
print(d)
# update 
u = d.update(leviet='thinhle')
print(u)
print(d)