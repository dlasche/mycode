#!/usr/bin/env python3

#Restful API is?

import urllib.request
import json

URL = 'https://thedogapi.com/v1/images/search'

webobj = urllib.request.ulropen(URL)
webobj = requests.get(URL).json()

content = webobj.read()


atlast = json.loads(content.decode('utf-08'))

print(atlast[0]['url'])
print(type(atlast))

