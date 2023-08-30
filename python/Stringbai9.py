# nối 2 chuỗi %s % || %s được định nghĩa bởi kteam || input nhiều hơn thì thêm , 
a = ' My team is %s %s years old '%('1','2')
print(a)

# tái sử dụng biến 
x = '%s %s'
result = x % ('D','2')
print(result)

# %d lấy phần nguyên 
# %f lấy tất cả số (số thực )

f = '%.f' %(3.5999)
print(f)

#
print(f'a\tb')

#f'{} tìm biến để gắn vào 
k ='Kteam'
newResult = f'{k} - free edu'
print(newResult)
#example 
name = 'quoc '
midname = 'thinh'
use = f'my name: {name}{midname} '
print(use)
# định dạng thì thêm 2 dấu nhọn 
# f‘1: {{one}}, 2: {{two}}, 3: {variable}’
# output : ‘1: {one}, 2: {two}, 3: three’


# định dạng bằn fomat và tăng tính thẩm mĩ trong code 
r = 'a: {1}, b: {2}, c: {0}'.format('one', 'two', 'three')
print(r)

q = 'name {:*^50} '.format('quoc thinh')
print(q)

#{:<10}'.format('aaaa') # căn lề trái
#{:>10}'.format('aaaa') # căn lề phải


# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Kteam', 'TP HCM')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Kquiz', 'Da Lat')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)

# bản thân vẫn là kiểu chuỗi sau khi ép kiểu ||
c = '12'
print(int(12))
print(type(a))
# in hoa string chữ đầu ( capitalize )
a = 'le viet quoc thinh '
b = a.capitalize()
print(a)
print(b)

