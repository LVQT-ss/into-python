def reverse_number(n):
    n_string = str(n)
    if "-" in n_string:
        n_string = n_string[1:]
        return int('-' + n_string[::-1])
    else :
        return int(n_string[::-1])
    
    # https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/train/python