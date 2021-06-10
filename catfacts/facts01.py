#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():
    """Run Code"""
    # create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    # json() method will dump a JSON string into Pythonic data structure
    print(r.json())

main()
