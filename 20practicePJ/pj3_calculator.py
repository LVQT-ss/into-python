def add(a,b):
    answer = a +b 
    print(str(a)+" + "+ str(b) + " = "+str(answer))
def sub(a,b):
    answer = a -b 
    print(str(a)+" - "+ str(b) + " = "+str(answer))
def mul(a,b):
    answer = a *b 
    print(str(a)+" * "+ str(b) + " = "+str(answer))
def div(a,b):
    answer = a/b 
    print(str(a)+" / "+ str(b) + " = "+str(answer))
while True:

    print("A.addition")
    print("B. Subtraction")
    print("C. Mul")
    print("D. div")
    print("E. exit")

    choice = input("input your choice:")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        add(a,b)
    elif choice == "b" or choice == "B":
        print("subtraction")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        sub(a,b)
    elif choice == "c" or choice == "C":
        print("Multication")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        mul(a,b)
    elif choice == "d" or choice == "D":
        print("division")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        div(a,b)
        quit()