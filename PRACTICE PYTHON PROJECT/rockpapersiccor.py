# game kéo búa bao 
from random import randint
nguoi=int(input('Bạn vui lòng chọn : \n 1. kéo 2. búa 3.bao \n'))
may=randint(1,3)
if may == 1: 
    print('máy chọn kéo ')
if may == 2: 
    print('máy chọn búa ')
if may == 3: 
    print('máy chọn bao ')

if may == nguoi :
    print('---- TIE----')
if may == 1 and nguoi==2:
    print('------WIN----')
if may ==1 and nguoi==3:
    print('-----LOSE-----')
if may == 2 and nguoi==3:
    print('------WIN----')
if may ==2 and nguoi==1:
    print('-----LOSE-----')
if may == 3 and nguoi==1 :
    print('------WIN----')
if may ==3 and nguoi==2:
    print('-----WIN-----')