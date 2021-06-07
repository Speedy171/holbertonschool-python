#!/usr/bin/python3

"""
Lists 10 commits sorted from the recent to the oldest in the repository
rails by the user rails
"""

import requests
from sys import argv

if __name__ == "__main__":
    github_commits = 'https://api.github.com/repos/'\
    + argv[2] + '/' + argv[1] + '/commits'
    data = {'per_page':10, 'page':1}
    req = requests.get(github_commits, data)
    res = req.json()

    for r in res:
        print(r.get('sha') + ': ', end="")
        print(r.get('commit').get('author').get('name'))
