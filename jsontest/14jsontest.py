#!/usr/bin/env python3

import requests

TIMEURL = 'http://time.jsontest.com/'

def main():
    t = requests.get(TIMEURL).json()
    print(f"""current time is:
    Date: {t['date']}
    Epoch: {t['milliseconds_since_epoch']}
    Time: {t['time']}""")

