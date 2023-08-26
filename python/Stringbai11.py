# tách chuỗi spilt sau , là cắt bao nhiêu lần 
a = 'le viet quoc thinh'
b = a.split('e',1)
print(b)
# partition  trả về chuỗi trước và sau của ký tự 
c = a.partition('e')
print(c)
# count 
d = a.count('e',0,3)
print(d)

e=a.startswith('v',3)
print(e)

# tìm find 
f = a.find('t')
print(f)
# kiểm tra chuỗi 
g = a.isupper()
j = a.islower()
m=a.isdigit()
n=a.isspace()

# bài tập 
s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
q = s.strip('Aa').lstrip('AaOo').title()
print(q)