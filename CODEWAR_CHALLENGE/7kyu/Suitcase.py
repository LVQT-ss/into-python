def fit_in(side1,side2,length,width):
    combined = side1 + side2
    largest = max([side1,side2])
    if combined <= length:
        return largest <= width
    elif combined <= width:
        return largest <=length
    return False
    