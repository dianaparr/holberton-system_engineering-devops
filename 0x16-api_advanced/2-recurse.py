#!/usr/bin/python3
""" Module called 2-recurse """

import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Recursive function: This function queries the Reddit API and
        returns a list containing the titles of all hot articles for a
        given subreddit.
    """
    HEADERS = {'User-Agent': 'HotReddit/1.0.1'}
    LIMIT = 100
    URL = 'https://www.reddit.com/r/{}/hot.json?limit={}&after={}'.format(
        subreddit, LIMIT, after)
    r = requests.get(URL, headers=HEADERS, allow_redirects=False)
    if r.status_code >= 400:
        return None
    response_json = r.json()
    # ‘Listing’ represents a list of things
    if response_json['data']['children'][0]['kind'] == 't3':
        for post in response_json['data']['children']:
            hot_list.append(post['data']['title'])

    #  base case
    after = response_json['data']['after']
    # If it equals None it is because there is no page after,
    #  the last result was extracted
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
