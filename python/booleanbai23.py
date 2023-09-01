print(3>1)
print(241==141 +100)
print((5 * 0) != 0 )
print('kteam'== 'kteam')
# dùng ascii để in ra ord()
print(ord('a'))
o = [ord(char) for char in 'ABC']
print(o)

print('a'>'ABC')

# IS không phải là == mà là kiểm tra có phải nó là chính nó không 
# hàm IS là dùng id để so sánh chứ không phải thứ mà mình thấy là giống
lst = [1,2,3]
lst_ = [1,2,3]

print(lst is lst_)
print(id(lst))
print(id(lst_))

# bản chất của tất cả giá trị đều chuyển về boolean được hết và là true
# còn những giá trị rỗng không có thì tất cả là false 
print(bool(0))
print(bool(None))
print(bool(True))
print(bool(False))