def get_ages(sum_, difference):
    age1=(sum_+difference)/2
    age2 = age1- difference 
    
    if sum_ <0  or difference <0:
        return None
    elif sum_ == difference : 
        return sum_ , 0
    else:
        return age1,age2
    