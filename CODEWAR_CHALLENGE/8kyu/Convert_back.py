def abbrev_name(name):
    words = name.split(' ')
    letters = [word[0].upper() for word in words]
    return '.'.join(letters)

# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python