n = "this is a test function"
n = n.split(" ")  # Split the string into a list of words
n = [word.capitalize() for word in n]  # Capitalize each word in the list
n = " ".join(n)  # Join the capitalized words back into a single string
print(n)
