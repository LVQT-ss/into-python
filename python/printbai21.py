print('le viet','quoc thinh' , 69)
print('le','viet','quoc','thinh',sep='---')

# end|| dùng để in trong cùng 1 dòng 
print('line 5 ')
print('line 6 ')
print('line 7 ')

print('123',end='')
print('456')



# cách cho chương trình đợi 3 giây rồi mới chạy thì dùng import thư viện sleep 
from time import sleep 

print('start..;')
sleep(3)
print('end')
# dừng chương trình thì dùng end 
from time import sleep
print('start..;',end='')
sleep(3)
print('end')
# flush 
from time import sleep 

print('start..;',end='',flush=True)
sleep(3)
print('end')
# ghi vào file 
with open('printtext.txt','w') as f:
    print('printed by print function', file = f )

# test thử 
from time import sleep

your_name=' ha tan phat'
your_greet='sữa tươi nguyên chất tuyệt trùng từ '

for c in your_greet + your_name:
    print(c,end='',flush=True)
    sleep(0.1)
print()