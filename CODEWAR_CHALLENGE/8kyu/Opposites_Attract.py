def lovefunc( flower1, flower2 ):
    fi = flower1 % 2 
    se = flower2 % 2 
    if (fi!=0 and se == 0) or (fi ==0 and se != 0 ) :
        return True
    else:
        return False