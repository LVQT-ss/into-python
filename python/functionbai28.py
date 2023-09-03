def quocthinh():
    print('hello quocthinh')
quocthinh() 
for _ in range(3):
    quocthinh()

def hello():
    print('hello kteam')

    print('free education')

for _ in range(8):
    hello()

# hàm có parameter | tham số đầu vào 
def thinh(text,age):
    print(text)
    print(age)

thinh('levietquocthinh ',20)
# danh sách các default parameter phải ở cuối cùng ở danh sác 
def kteam(age,text='kter'):
    print(text)
    print(age)

kteam(69)
kteam(10,'k9')


# biến cục bộ chỉ xài trong phạm vi chứa trong nó 
# biến toàn cục 
def f(ktea=[]):
    ktea.append('F')
    print(ktea)

f()
f()
f()