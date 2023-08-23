def main():
    print("hello world ")
     
    
    x = 'how are you'
    y = x.upper()
    print(y)


    n= 5
    m =10 
    number=[1,2,3,4]
    names= ["thinh","thai"]
    print(names)
    number.append(10)
    print(number[0])
    print(len(number))
    name="thinh"
    cau_chao="hello,world"
    print(cau_chao.split(","))
    print("hello" in cau_chao)


    age = 40
    if age < 18:
        print(' chua du 18 tuoi ')
    elif age < 30:
        print("hang lanh manh cho thanh nien duoi 30 ")
    else :
        print('hang lanh manh cho nguoi lon ')



    i= 0 
    while i < 10:
        print('my steam account')
        i=i+1

    cac_web_hay=["anime.moe","phimmoiz.net"]
    for web_hay in cac_web_hay:
        print(web_hay)


def tinh_tong(l):
    tong = 0 
    h = 1 
    while h <= l:
        tong = tong + h
        h = h + 1

    return tong



if __name__ == "__main__":
    main()
    print(tinh_tong(50))