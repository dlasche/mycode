#!/usr/bin/env python3

import os

## define a function that stops searching on first match
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

lookfor = input('Waht am I looking for?:')
lookwhere = input('Waht is the path in which I should be searching?:')

print(find(lookfor, lookwhere))
