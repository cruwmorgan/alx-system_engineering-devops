#!/usr/bin/python3
"""recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords (
case-insensitive, delimited by spaces. Javascript should count as javascript,
but java should not).
"""
from collections import OrderedDict
from requests import get


def count_words(subreddit, word_list, after=None, match_dict={}):
    try:
        url = 'https://www.reddit.com/r/{}/hot.json?limit=100&&after={}'\
           .format(subreddit, after)
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
            Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
        }
        response = get(url, headers=headers, allow_redirects=False)
        reddits = response.json()

        if word_dict == {}:
            for i in word_list:
                word_dict[i] = 0

        after = reddits.get('data').get('after')

        children = reddits.get('data').get('children')
        for title in range(len(children)):
            title_ref = children[title]['data']['title']
            search_list = title_ref.split()
            for word in search_list:
                for i in word_list:
                    if i.lower() == word.lower():
                        word_dict[i] += 1

        if after is None:
            order_dict = OrderedDict(sorted(word_dict.items(),
                                            key=lambda x: x[1],
                                            reverse=True))
            zero_count = 0
            for k, v in order_dict.items():
                if v != 0:
                    print("{}: {}".format(k, v))
                else:
                    zero_count += 1
            if zero_count == len(order_dict):
                print()

        else:
            count_words(subreddit, word_list, after, word_dict)

    except:
        pass
