#!/usr/bin/env python3

round = 0
while True:
    round += 1
    print('Finish the movie title, "Monty Python \'s The Life of ______"')

    answer = input('Your guess-->')
    if answer =='Brian':
        print('Correcft')
        break
    elif round==3:
        print('Sorry, the answer was Brian.')
        break
    else:
        print('sorry! Try again!')

