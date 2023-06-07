#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
from json import loads
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100&&after={}'\
           .format(subreddit, after)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    response = get(url, headers=headers, allow_redirects=False)
    reddits = response.json()

    try:
        children = reddits.get('data').get('children')
        for title in range(len(children)):
            hot_list.append(children[title]
                            ['data']['title'])

        after = reddits.get('data').get('after')
        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)

    except:
        return None
