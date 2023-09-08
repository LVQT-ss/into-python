def rental_car_cost(d):
    if d >= 7:
        return ((d * 40)-50)
    elif  7 >= d >= 3:
        return ((d*40)-20)
    else :
        return d*40
    
    # https://www.codewars.com/kata/568d0dd208ee69389d000016/solutions/python