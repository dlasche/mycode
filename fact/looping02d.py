#!/usr/bin/env python3

#open a file in python
with open('dnsservers.txt', 'r') as dnsfile:
    #indent to keep open
    #loop across the lines of the file
    for svr in dnsfile:
        svr = svr.rstrip('\n') # remove newline char if exists
        #would exist on all but last line
        #IF svr ends with 'org'
        if svr.endswith('org'):
            with open('org-domain.txt', 'a') as srvfile:
                srvfile.write(svr + '\n')
         #ELSE-IF string ends with 'com'
        elif svr.endswith('com'):
            with open('com-domain.txt', 'a') as srvfile:
                srvfile.write(svr + '\n')
#file closed automatically


