#!/usr/bin/env

import csv

run = input('Welcome! This is a Database of comic books spanning the Marvel and DC Universe. We can create a list of Comics by author for you. Press x to quit, or spacebar to continue: > ')
if run == 'x':
    quit()

with open('brett_comics.txt', 'r') as comicfile:
    #pull data from csv file.
    #write a new file including all the relevant information
    #This code will parse through the comic book 'library' and return a select few that match the search parameters
    author = input("""Select what author\'s works you would like to view:
                    1.
                    2. 
                    3.
                    >""").title()
    comic_lines = comicfile.readlines()
    filename = 'testdoc.rc'
    with open(filename, 'w') as rcfile:
        for line in comic_lines:
            if author in line:
                print(f'{line}', file=rcfile)



print('Your list of comicbooks by author has been created!')
