#!/usr/bin/env python3
import os

for root,subdirs,files in os.walk('/home/student/mycode/'):
    if "treewlaker.py" in files:
        print('Tree wlkaer found!')

    print(root,subdirs,files)


    

