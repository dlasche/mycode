#!/usr/bin/env python3
"""This a number guessing game between 1 and 100.
Written by: Daniel Lasche"""

import random
rand =  random.randint(1, 100)

# 5 guesses, input, while loop? 

count = 0

while count  < 5:
   try:
       guess = int( input('Choose a number between 1 and 100'))
       if guess == rand:
           print('You got it! Congratulations')
           break
       elif guess > rand:
           print('You\'re wrong! Too high.')
           count += 1
       else :
           print('You\'re wrong! Too low.')
           count += 1
   except:
       print('That is not a number. Please input a number.')

