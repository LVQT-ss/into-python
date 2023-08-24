'''
đây là chú thích 
'''
strfullname= "i'm levietquocthinh'"

print(strfullname)
print(type(strfullname))

# cách xuống dòng trong chuỗi 
n = """
đây là chuỗi thứ 1 
đây là 2 
đây là 3 
"""
print(n)


n = " đây là chuỗi thứ 1 \n đây là 2 \n đây là 3 "

print(n)
print('\a') # câu lệnh này kêu tiếng bíp 

# in ra dấu \ chuỗi trần "r" trong C sharp là @ 
print(r'haizz, \neu mot ngay nao do ')

# nối 2 chuỗi 
strA = "le viet"
strB = "quoc thinh "
strC = strA + strB*3 
print(strC)
# kiểm tra chuỗi true hay false "in"
print("le" in strA )
# đếm chuỗi bằng len 
print(len(strA))
# lấy ra ký tự đầu tiên của chuỗi 
print(strA[0])
# lấy ra ký tự cuối cùng của chuỗi 
print(strA[len(strA) -1 ])
# cắt chuỗi 
print(strA[3:len(strA)])
print(strA[3:None])
# thay đổi giá trị trong chuỗi 

strE = "HowKteam.com"
strE = strE[None:1]+"0" + strE[2:None]
print(strE)
# ép kiểu 
i = float("6") + 5 
b = str(6) + "5"
print(i)
print(b)







