def correct(s):
    mistakes = { 
    '0' : 'O',
    '5' : 'S',
    '1' : 'I'
    }
    return ''.join(mistakes.get(char,char) for char in s)

# https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/python
# phương thức join để nối chuỗi 