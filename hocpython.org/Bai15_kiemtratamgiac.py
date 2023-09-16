a = int(input("nhập vào lương tháng này : \n"))
b = int(input("nhập vào lương tháng này : \n"))
c = int(input("nhập vào lương tháng này : \n"))
if a+b > c and a +c > b and b +c > a :
    print("abc là tam giác")
else:
    print("không có tam giác")