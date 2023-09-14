def bumps(road):
    total = sum([1 if char == 'n' else 0 for char in road.lower()])
    if total <= 15:
        return 'Woohoo!'
    return 'Car Dead'
# https://www.codewars.com/kata/57ed30dde7728215300005fa/train/python