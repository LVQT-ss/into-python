

s ="bitcoin take over the world maybe who knows perhaps"
s = s.split(' ')
char_counts = [len(item) for item in s]
sort = sorted(char_counts)
print(sort[0])


