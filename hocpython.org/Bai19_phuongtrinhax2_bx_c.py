a = float(input("nhập vào lương tháng này : \n"))
b = float(input("nhập vào lương tháng này : \n"))
c = float(input("nhập vào lương tháng này : \n"))
print("phương trình " + str(a) +"x^2+ "+str(b)+"x+"+str(c)+"=0")
if a == 0 :
    if b == 0 : 
        if c == 0:
            print("đây là phương trình vô số nghiệm")
        else:
            print('đây là phương trình vô nghiệm')
    else:
        print("phương trình có 1 nghiệm",-c/b)
else : 
    delta = b ** 2 - 4 * a * c 
    if delta > 0 :
        candelta = delta**0.5
        x1 = (-b + candelta)/(2*a)
        x2 = (-b - candelta)/(2*a)
        print("phương trình có 2 nghiệm phân việt là ", x1 ,x2)
    elif delta == 0 : 
        print("phương trình có ngghiem kep la:" ,-b/(2*a))
    else:
        print("phương trình vô nghiệm")
