#!/usr/bin/env python3

import requests

AOIF = "https://www.anapioficeandfire.com/api"

def main():
    ## send HTTPS GET to the API of ICE and FIRE
    gotresp = requests.get(AOIF)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    print(got_dj)

if __name__ == '__main__':
    main()
