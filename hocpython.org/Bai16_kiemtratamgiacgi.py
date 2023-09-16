a = int(input("nhập vào a : \n"))
b = int(input("nhập vào b : \n"))
c = int(input("nhập vào c : \n"))
if a+b > c and a +c > b and b +c > a :
    if ( a == b ==c ):
        print("abc là tam giác đều")
    elif (a==b or a==c or b ==c ):
        if(a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2 ):

            print("tam giác vuông cân")
        else : 
            print("a b c tạo thành tam giác vuông")
    elif (a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2 ):
        print(" tam giác vuông ")
    else : 
        print(" tam giác thường")
else:
    print("không thể tạo thành tam giác")