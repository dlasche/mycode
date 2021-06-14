#!/usr/bin/env python3

"""Script to search for a pattern match"""

import os
import fnmatch
import argparse


EXCLUDE = ["/usr", '/home', '/var']

def find(pattern, path):
    """search through filesystem based on given path location"""
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE:
            dirs[:] = []
            files[:] = []
        for name in files:
            if fnmatch.fnmatch(name.lower(), pattern.lower()): # if match
                result.append(os.path.join(root, name)) #add to list
    return result

def main():
    """run time code"""
    parser = argparse.ArgumentParser(description='Find files by name/location')
    parser.add_argument('-n', help='The name of the file you\'re looking for.')
    parser.add_argument('path', help='The directory we start the search.')
    args = parser.parse_args()

    lookfor = args.n
    lookwhere = args.path
#    lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg ")
#    lookwhere = input("What is the path in which I should search? ")
    print("Results: ", len(find(lookfor, lookwhere))) # call function

main()

