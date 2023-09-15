def pattern(n): 
    # your code here
    triangle = []
    
    for row in range(1,n+1):
        triangle.append(' ' * row + ' '.join([str(row % 10 )] * ( n - row +1 ))) 
    return '\n'.join(triangle)
    
print(pattern(10))