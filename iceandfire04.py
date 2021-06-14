#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)
        
        ## make api request for house name
        house = got_dj['allegiances'][0]
        print(house)
        got_alleg = requests.get(house).json() # needed to translate JSON to python, I added .json() at end
        print(got_alleg.get('name')) # you were missing the ) at the end, which was what was causing the "if name = main thing"

        ## books
        books = got_dj['books']
        char_books = []
        for book in books:
            current_book = requests.get(book).json().get('name')
            char_books.append(current_book)
        pov_books = got_dj['povBooks']
        for book in pov_books:
            current_pbook = requests.get(book).json().get('name')
            if book not in char_books:
                char_books.append(current_pbook)
        print(char_books)


            


if __name__ == "__main__":
    main()

