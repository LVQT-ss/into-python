def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    return [bird for bird in birds if not bird in geese]

# https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python