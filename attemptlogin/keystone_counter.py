#!/usr/bin/env python3

loginfail = 0

keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", 'r')
#turn file into list of lines in memory

keystone_file_lines = keystone_file.readlines()
#loop over lines

for line in keystone_file_lines:
    #if fail pattern appears:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1
print('The number of failed log in attempts is', loginfail)
keystone_file.closed()

