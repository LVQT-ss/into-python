def array(string):
    numbers = string.split(',')
    numbers = numbers[1:-1]
    if len(numbers)==0:
        return None
    return ' '.join(numbers)

# https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python

# def remove_char(s):
#    return s[1:-1]