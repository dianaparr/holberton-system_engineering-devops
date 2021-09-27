#!/usr/bin/python3
""" Module called 0-subs """

import requests


def number_of_subscribers(subreddit):
    """ This function queries the Reddit API and returns the number of subscribers
        (not active users, total subscribers) for a given subreddit.
    """
    # Identify the PI version with the user Agent request header
    HEADERS = {'User-Agent': 'UserReddit/0.0.1'}
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(URL, headers=HEADERS)
    if r.status_code == 200:
        response_json = r.json()
        return response_json['data']['subscribers']
    return 0
