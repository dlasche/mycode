#!/usr/bin/env python3

import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    # display the method s available to our new object

    print(dir(r))

main()

