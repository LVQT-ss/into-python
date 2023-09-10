#https://www.codewars.com/kata/56d0a591c6c8b466ca00118b/train/python

def is_triangular(t):
    level = 1
    while t > 0 : 
        t -= level 
        level += 1 
    return t == 0 

print(is_triangular(3))