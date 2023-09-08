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
# reversed the word if the word have the length equal or more than 5 
# reversed = [::-1]
def spin_words(sentence):
    words = sentence.split(" ")
    words = [word[::-1] if len(word) >=5 else word  for word in words]
    return " ".join(words)

#duplicate letter in string 
def duplicate_count(text):
    occured = []
    found = []
    counter = 0
    for letter in text:
        if letter.lower() not in occured:
            occured.append(letter.lower())
        else:
            if letter.lower() not in found:
                counter+=1
                found.append(letter.lower())
    return counter
