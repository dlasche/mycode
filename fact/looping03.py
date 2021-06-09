#!/usr/bin/env python3
#this library allows us to generate UUID values.

import uuid

howmany = int(input('How many UUIDs shoud be generated? '))

print('Generating UUIDS...')

# range is required because an int cannot be looped
for rando in  range(howmany):
    print( uuid.uuid4() )


