#!/usr/bin/python3
"""Module that checks the subscribers count of a specific subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Sends a request to the reddit api to check the count of a specific
    subreddit subscribers
    """

    count = 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "script (by /u/sheko100)"}

    res = requests.get(url, headers=headers)
    if res.status_code == requests.codes.ok:
        json = res.json()
        count = json["data"]["subscribers"]

    return count
