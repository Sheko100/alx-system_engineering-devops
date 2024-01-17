#!/usr/bin/python3
"""Module that checks the subscribers count of a specific subreddit
"""

import requests


def top_ten(subreddit):
    """Sends a request to the reddit api to print the titles of top ten posts
    titles for a specific subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "script (by /u/sheko100)"}

    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print(None)
    else:
        json = res.json()
        posts = json["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
