#https://www.codewars.com/kata/56d0a591c6c8b466ca00118b/train/python

def is_triangular(t):
    # Initialize the level variable to 1.
    level = 1
    
    # Use a while loop to check if t is greater than 0.
    while t > 0:
        # Subtract the current level from t.
        t -= level
        
        # Increment the level by 1 for the next iteration.
        level += 1
    
    # Check if t has become 0 after the loop.
    # If t is 0, then it's a triangular number, so return True.
    # Otherwise, return False.
    return t == 0

print(is_triangular(6))