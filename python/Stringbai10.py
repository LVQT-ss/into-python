a = ' le viet quoc thinh'
# uppper and lower và swapcase()
b= a.capitalize()
c = a.upper()
d = a.lower()
e = a.swapcase()
f = a.title()
g= a.center(30,'-')
h = a.rjust(50,'-')
i = a.ljust(50,'-')
l = a.join(['1','2','3','4'])
m= a.replace('e','E', 1)
# strip xóa các kí tự đầu và cuối 
n = a.strip()
print(b+'\n' +c + '\n' + d + '\n' + e + '\n' + f+'\n'+ g +"\n"+h +"\n"+i+'\n'+l+'\n'+m)
print(n)
k= 'cái gì v '
j = k.encode(encoding='utf-8',errors='strict')
print(j)