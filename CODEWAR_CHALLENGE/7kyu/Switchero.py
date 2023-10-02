def switcheroo(s):
    output=""
    for char in s : 
        if char =='a':
            output += 'b'
        elif char =='b':
            output += 'a'
        else :
            output += char 
    return output 