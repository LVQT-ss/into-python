def procedure(i):
    multiples = list(range(i,101,i))
    
    multiples_string = [str(n) for n in multiples]
    
    digit_sums = []
    
    for number_string in multiples_string:
        print(number_string)
        digit_sum = sum([int(d) for d in number_string])
        digit_sums.append(digit_sum)
        
    sum(digit_sums)

print(procedure(2))