def expression_matter(a, b, c):
    operations =[
        a * ( b + c ),
        a * b * c,
        a + b * c,
        (a + b ) * c,
        a + b +c 
    ]
    return max(operations)

# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/python