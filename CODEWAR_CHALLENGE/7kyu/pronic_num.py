def is_pronic(n):
    
    if n <0 :
        return False
    if n == 0 :
        return True
    for i in range(1,n+1):
        if i * (i+1) == n :
            return True
    return False

# https://www.codewars.com/kata/55b1e5c4cbe09e46b3000034/solutions/python