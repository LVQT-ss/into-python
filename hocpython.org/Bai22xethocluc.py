toan = int(input("nhap vao toan :"))
van = int(input("nhập vào van :"))
anh = int(input("nhap vao anh :"))
if ( 0 <= toan <= 10 and 0 <= van <=10 and 0<= anh <= 10):
    dtb = (toan + van + anh )/3
    if dtb >=8 and (toan >=8 or van >=8) and ( toan >= 6.5 and van >=6.5 and anh >=6.5):
        print("hoc sinh gioi")
else:
    print("nhap sai") 