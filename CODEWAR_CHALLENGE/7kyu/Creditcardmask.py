# return masked string
def maskify(cc):
    if len(cc) < 5 : 
        return cc 
    else : 
        result = ""
        result += ((len(cc)-4)*'#')+cc[-4:]
        return result 
    
print(maskify('112112231231231'))