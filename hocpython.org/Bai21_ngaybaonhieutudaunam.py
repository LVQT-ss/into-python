ngay = int(input("nhap vao ngay :"))
thang = int(input("nhập vào nâm :"))
if thang <= 8:
    sothang30ngay = (thang-1) //2 
    sothang31ngay = thang//2 
else:
    sothang30ngay = thang //2 
    sothang31ngay = (thang+1)//2
songay = ngay + sothang30ngay*30 + sothang31ngay*31
if thang > 2:
    songay -= 2
print(songay)