#!/usr/bin/env python3

#creata a list called vendors

vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista']

approved_vendors = ['cisco', 'juniper', 'big_ip']

#loop across the list vendors

for x in vendors:
    print('The vendor is:' + x, end='')
    if x not in approved_vendors: 
        print(' - NOT AN APPROVED VENDOR!', end='')
print('\nOur loop has ended.')

