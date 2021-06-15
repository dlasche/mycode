#!/usr/bin/env python3

import json
import requests


def main():
    start_date = input('start date (format 2021-06-12):')
    end_date = input('end date (format 2021-06-12):')
    api_key = ''
    with open('/home/student/nasa.creds') as mycreds:
        api_key = mycreds.read()
    
    api_key = "api_key=" + api_key.strip('\n')

    NASAAPI = "https://api.nasa.gov/neo/rest/v1/feed?start_date=" + start_date + "&end_date=" + end_date + "&" + api_key

    

    get_api = requests.get(NASAAPI).json()

    number_of_ast = get_api.get('element_count')
    print(number_of_ast)

    closest = 9999999999999999999999

    #for dates in get_api['near_earth_objects']:
     #   for x in get_api['near_earth_objects'][dates]:
    print("""
    Biggest:
    Speediest:
    Closest:
    Needed Bruce Willis for 
    """)

    
    


if __name__ == '__main__':
    main()

