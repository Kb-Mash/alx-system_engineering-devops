#!/usr/bin/python3
"""module of the function number_of_subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit using
    the Reddit API.

    Args:
        subreddit (str): The name of the subreddit for which to
        retrieve subscriber count.

    Returns:
        int: The number of subscribers for the specified subreddit,
        or 0 if not found or an error occurs.
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
