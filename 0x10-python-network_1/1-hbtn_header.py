#!/usr/bin/python3

"""
Get the value of the header X-Request-Id of the given url
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
