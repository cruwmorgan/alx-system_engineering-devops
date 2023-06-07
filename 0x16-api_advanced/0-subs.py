#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of
subscribers
"""
from json import loads
from requests import get


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    response = get(url, headers=headers)
    reddits = response.json()

    try:
        subscribers = reddits.get('data').get('subscribers')
        return int(subscribers)
    except:
        return 0
