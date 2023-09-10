def fly_by(lamps, drone):
    the_length_of_the_flight_path = len(drone)
    return ''.join(['o' if i  < the_length_of_the_flight_path else 'x' for i in range(len(lamps))])

print(fly_by('xxxxxx', '====T'))