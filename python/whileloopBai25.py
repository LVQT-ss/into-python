k = 5 
while k > 0:
    print('k=',k)
    k-=1

s= 'le viet quoc thinh'
idx= 0 
length= len(s)
while idx < length:
    print(idx, ' stands for ', s[idx])
    idx +=1

five_even_numbers =[]
k_number = 1

while True: # vòng lặp vô hsn5 vì giá trị ở đây là hằng số 
    if k_number % 2 == 0: # nếu k_number là một số chẵn 
        five_even_numbers.append(k_number)# thêm giá trị của knumber vào list
    if len(five_even_numbers) == 5:# nếu list này đủ 5 phần tử
            break# thì kết thúc  vòng lặp
    k_number +=1
print(five_even_numbers)
print(k_number)

a_number =1
while a_number < 10:
    if a_number %2 == 0:
          a_number +=1
          continue
    print(a_number,'is odd number')
    a_number +=1

print(a_number)

# rút gọn code 
a_number = 1 
while a_number < 10:
    a_number +=1
    if a_number %2 == 0:
          continue
    print(a_number,'is odd number')
print(a_number)


# while else 
k=0
while k< 3:
     print('value of k is ',k)
     k+=1
else:
     print('k is not less tan 3 anymore')

    
i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Bỏ qua 3")
        continue
    print(i)

# ------------------ BÀI TẬP CỦNG CỐ--------------------
# bài 1 
print('-------------bai 1 ---------------')
even_number= []
s_number=1
while len(even_number) < 5: 
    if s_number % 2 == 0:
        even_number.append(s_number)
    s_number+=1
print(even_number)


# bai 2 
print('\n ------------------------------------------------------')

with open('draftWHILEELSE.txt') as filebt:

    lst = list(filebt)

    filemoi = ''

    for data in lst:

        data2 =  data.split()

        for ind in range(len(data2)):

            if data2[ind] == 'Kteam':

                data2[ind-1] = 'How'

        dongmoi = ' '.join(data2)            

        filemoi = f'{dongmoi}'

        print(filemoi)

with open('kteam.txt', 'w') as complete:

    print(complete.write(filemoi))



print(' ------------------------------------------------------')




# bai 3 
print('------------bai 3 - --------')
mang = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]
k=0
mang1=[]
mang2=[]
while k < len(mang):
    if mang[k] !=11:
        mang1.append(mang[k])
    else:
        mang2.append(k)
    k+=1
mang1.sort()
i=0
while i < len(mang2):
    mang1.insert(mang2[i],11)
    i+=1
print(mang1)