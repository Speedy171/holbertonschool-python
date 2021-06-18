#!/usr/bin/python3
"""
0-count.py
"""

from collections import Counter, defaultdict
import re
import requests


def count_words(subreddit, word_list, res=defaultdict(int), after=None):
    """Counting the words in Subreddit"""
    agent = "linux:1:v2.1 (by /u/heimer_r)"
    headers = {"User-Agent": agent}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)
    try:
        req = requests.get(url, headers=headers, allow_redirects=False).json()
        titles = req.get('data').get('children')
        for title in titles:
            count = Counter(title.get('data').get('title').lower().split(' '))
            for x in word_list:
                if x.lower() in count:
                    res[x] += count.get(x.lower())
        after = req.get('data').get('after')
        if after:
            return count_words(subreddit, word_list, res, after)
        sort_first = sorted(res.items(), key=lambda x: x[0])
        for k, v in sorted(sort_first, key=lambda x: x[1], reverse=True):
            print('{}: {}'.format(k, v))
    except:
        return
