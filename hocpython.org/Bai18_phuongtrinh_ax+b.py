a = float(input("nhập vào lương tháng này : \n"))
b = float(input("nhập vào lương tháng này : \n"))
print("phương trình " + str(a) +"x+ "+str(b)+" = 0")
if a == 0 :
    if b == 0 : 
        print("phương trình vô số nghiệm")
    else:
        print("phương trình vô nghiệm")
else: 
    print("nghiệm của phương trình là ",-b/a)