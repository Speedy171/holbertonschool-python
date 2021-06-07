
#!/usr/bin/python3

"""
Get X-Request-Id found in the header of given URL
"""

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('X-request-id'))
