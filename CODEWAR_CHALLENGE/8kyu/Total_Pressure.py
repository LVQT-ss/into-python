def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    temp_kelvin = 273.15 + temp
    num = (given_mass1 / molar_mass1 + given_mass2 / molar_mass2) * temp_kelvin *0.082
    return num / volume
    
# https://www.codewars.com/kata/5b7ea71db90cc0f17c000a5a/solutions/solutions
