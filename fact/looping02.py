#!/usr/bin/env python3
#open file in read mode

with open('dnsservers.txt', 'r') as dnsfile:
    #create list of lines
    #loop over lines of file
    for svr in dnsfile:
        #print and end without a newline
        print(svr, end='')
#no need to close your file

