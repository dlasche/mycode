#!/usr/bin/env python3

import requests

URL = 'http://api.open-notify.org/astros.json'

def astronauts():

    r = requests.get(URL).json()

    print('People in Space:', r.get('number'))
    for astronaut in r.get('people'):
        print(f"{astronaut.get('name')} is on the {astronaut.get('craft')}.")

def main():
    astronauts()

if __name__=='__main__':
    main()


