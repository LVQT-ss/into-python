def DNA_strand(dna):
    output_string = ""

    for char in dna:
        if char == 'A':
            output_string += 'T'
        elif char == 'T':
            output_string += 'A'
        elif char == 'C':
            output_string += 'G'
        elif char == 'G' :
            output_string += 'C'
        else:
            output_string += char
    return output_string

