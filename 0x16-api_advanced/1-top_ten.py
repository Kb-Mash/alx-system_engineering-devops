#!/usr/bin/python3
"""module of the function top_ten"""
import requests


def top_ten(subreddit):
    """
     Retrieve and print the titles of the top ten hot posts for a
     given subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit for which to
        retrieve the top ten hot posts.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
