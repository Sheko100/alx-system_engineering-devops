#!/usr/bin/python3
"""Module that sends requests to the reddit API
"""

import requests


def count_words(subreddit, word_list):
    """Sends a request to the reddit api and returns a list of all hot
    aricles of a specific subreddit
    """

    after = ""
    count = ""
    metadata = subreddit.split()
    if len(metadata) > 1:
        if metadata[0] is not None and metadata[0].startswith("t3_"):
            after = "&after={}".format(metadata[0])
            subreddit = metadata[1]
        else:
            return None

    if len(hot_list) > 0:
        count = "&count={}".format(len(hot_list))

    url = "https://www.reddit.com/r/{}/hot.json?limit=100{}{}".format(
            subreddit, after, count
            )
    headers = {"User-Agent": "script (by /u/sheko100)"}
    posts_titles = []

    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        return None
    else:
        json = res.json()
        posts = json["data"]["children"]
        next_page = json["data"]["after"]
        metadata = "{} {}".format(next_page, subreddit)
        for post in posts:
            posts_titles.append(post["data"]["title"])
        hot_list = hot_list + posts_titles
        lst = recurse(metadata, hot_list)

    return hot_list
