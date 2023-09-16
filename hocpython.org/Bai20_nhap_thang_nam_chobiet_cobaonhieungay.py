thang = int(input("nhap vao thang :"))
nam = int(input("nhập vào nâm :"))
if thang ==1 or thang ==3 or thang== 5 or thang ==7 or thang == 8 or thang == 10 or thang == 12:
    print('tháng có 31 ngày ')
elif thang==4 or thang ==6 or thang == 9 or thang == 11:
    print("tháng có 30 ngày ")
else:
    if (nam%400 == 0) or (nam % 4 == 0 and nam % 100 !=0):
        print("thang co 29 ngay")
    else:
        print("thang co 28 ngày")