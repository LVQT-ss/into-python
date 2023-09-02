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

even_number= []
s_number=1
while len(even_number) < 5: 
    if s_number % 2 == 0:
        even_number.append(s_number)
    s_number+=1
print(even_number)


# bai 2 
print('\n ------------------------------------------------------')
file_path = r'C:\Users\Final stage\Desktop\python\python\draftWHILEELSE.txt'  # Replace with the actual path

try:
    file_object = open(file_path, 'r')  # 'r' for reading
    data = file_object.read()  # Read the first character

    #while True:
     #    if file_object

    file_object.close()  # Close the file after you're done reading
    print(data)

except FileNotFoundError:
    print("The file 'draftWHILEELSE.txt' does not exist.")

print(' ------------------------------------------------------')


# bai 3 
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