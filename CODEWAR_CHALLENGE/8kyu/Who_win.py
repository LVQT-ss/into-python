def uefa_euro_2016(teams, scores):
    first, second = teams
    msg= f'At match {first} - {second}, '
    if scores[0] == scores[1]:
        winner_msg = 'teams played draw.'
    elif scores[0] > scores[1]:
        winner_msg = f'{first} won!'
    else: 
        winner_msg= f'{second} won!'    
    msg += winner_msg
    return msg

# https://www.codewars.com/kata/57613fb1033d766171000d60/train/python