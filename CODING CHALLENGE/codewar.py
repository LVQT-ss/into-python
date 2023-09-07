# exclaimation marks là dấu chấm thang trong bài này thì mình sẽ xóa đi dấu '!' trong string 
def remove_exclamation_marks(s):
    return s.replace('!','')
# remove vowels 
def disemvowel(string_):
    vowels = 'aeiou'
    for v in vowels: 
        string_ = string_.replace(v,'')
        string_ = string_.replace(v.upper(),'')
    return string_
# 

text = ['Python', 'is', 'a', 'good', 'programming', 'language']

# nối chuỗi với dấu cách
print(' '.join(text))