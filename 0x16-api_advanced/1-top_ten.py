#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit"""

    if subreddit is None:
        return 0

    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "ALX project about advanced api"}

    response = requests.get(url, params={"limit": 10}, headers=user_agent)

    if response.status_code == 200:
        for post in response.json().get('data', {}).get('children', []):
            print(post.get('data').get('title'))
    else:
        print(None)
