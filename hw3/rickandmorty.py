#!/usr/bin/env python3
import requests
import asyncio
from operator import itemgetter

locations = []
r = requests.get('https://rickandmortyapi.com/api/location')
for place in r.json()['results']:
  locations.append({
    'id':place.get('id'),
    "name":place.get('name'),
     "type":place.get('type'),
    "dimension":place.get('dimension')
  })

characters = []
c = requests.get('https://rickandmortyapi.com/api/character')
for char in c.json()['results']:
  characters.append({
    'id':char.get('id'),
    "name":char.get('name'),
    "location":char['location'].get('name'),
    "status": char.get('status'),
    "species": char.get('species'),

    })

def showInstructions():
  #print a main menu and the commands
  print('''
====Explore the World of Rick and Morty====

Travel to any destination in the show, and meet 
characters that are located there!

========
Commands:
  portal (or p) 
  talk 
  dest (display destinations)
  info (display planet data)
''')

current_destination = locations[0]
def showStatus():
  #print the player's current status
  print('---------------------------')
  print('Welcome to ', current_destination.get('name'))

  

showInstructions()
# print(locations)
# print('characters:', characters)

#loop forever
# async def main():

while True:
    showStatus()

#get the player's next 'move'
#.split() breaks it up into an list array
#eg typing 'go east' would give the list:
#['go','east']
    move = ''
    while move == '':
        move = input('>')

# split allows an items to have a space on them
# get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    if move[0] == 'dest':
        for place in locations:
            print(place.get('name'), end=' -- ')
        print('\n')

    #if they type 'go' first
    if move[0] == 'portal' or move[0] == 'p':

        #check that they are allowed wherever they want to go
    
        destination = input("Destination:")
        # for place in r.json()['results']:
        #     if move[1] == place['name']:
        #         current_destination = place['name']
        #         print(current_destination)
        for place in locations:
            if destination == place.get('name'):
                current_destination = place
                print(current_destination.get('name'))
        #if locations.move[1] in locations.get('name')
        #set the current room to the new room
        #current_destination = locations[current_destination][move[1]]
        #there is no door (link) to the new room
        #else:
            #print('You can\'t go that way!')
    if move[0]  == 'info':
        print(f"""
                ID: {current_destination.get('id')}
                Name: {current_destination.get('name')}
                Type: {current_destination.get('type')}
                Dimension: {current_destination.get('dimension')}
                """)

    #if they type 'get' first
    if move[0] == 'talk':
        planet_characters = []
        for name in characters:
            if current_destination.get('name') == name.get('location'):
                print(name.get('name'), end=" -- ")
                planet_characters.append(name)
        print('\n')
        chosen_char = input("If you would like to learn more about a character, enter their name:")
        for name in planet_characters:
            if chosen_char == name.get('name'):
                print(f"""
                ID: {name.get('id')}
                Name: {name.get('name')}
                Location: {name.get('location')}
                Status: {char.get('status')}
                Species: {char.get('species')}
                """)
