#!/usr/bin/python3

"""
Sends the email to the given url
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    info = urllib.parse.urlencode({'email': argv[2]})
    info = info.encode('ascii')
    with urllib.request.urlopen(argv[1], info) as response:
        print(response.read().decode('utf-8'))
