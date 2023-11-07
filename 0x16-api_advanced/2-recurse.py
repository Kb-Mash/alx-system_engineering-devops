#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if subreddit is None:
        return None
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "ALX project about advanced api"}

    response = requests.get(url, params={"after": after}, headers=user_agent)

    if response.status_code == 200:
        after = response.json().get("data").get("after")
        if not after:
            return hot_list
        for post in response.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
        return recurse(subreddit, hot_list, after)
