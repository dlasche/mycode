#!/usr/bin/env python3

import os

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return root

lookfor = input("What am I looking for? ")
lookwhere = input("What is the path in which I should search? ")

print(find_all(lookfor, lookwhere))


