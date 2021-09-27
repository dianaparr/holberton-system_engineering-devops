#!/usr/bin/python3
""" Module called 1-top_ten """

import requests


def top_ten(subreddit):
    """ This function queries the Reddit API and and prints the titles of
        the first 10 hot posts listed for a given subreddit.
    """
    # Identify the API version with the user Agent request header
    HEADERS = {'User-Agent': 'HotReddit/0.0.1'}
    LIMIT = 10
    URL = 'https://www.reddit.com/r/{}/hot.json?limit={}'.format(
        subreddit, LIMIT)
    r = requests.get(URL, headers=HEADERS)
    if r.status_code == 200:
        response_json = r.json()
        for data in response_json['data']['children']:
            print(data['data']['title'])
    else:
        print(None)
