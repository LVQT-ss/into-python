def xo(s):
    s = s.lower()
    x = False
    y= False
    if 'x' not in s and not 'o' in s:
        return True
    
    x_counter = 0 
    o_counter = 0
    for i in s:
        if i =="x" :
            x_counter +=1 
        elif i =="o":
            o_counter +=1 
    if x_counter == o_counter:
        return True
    else :
        return False
    

    # easier method 
   # def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')