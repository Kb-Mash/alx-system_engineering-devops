#!/usr/bin/python3
""" module of the function count_words """
import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """
    Count occurrences of words in a subreddit's hot posts.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list): A list of words to search for.
        hot_dict (dict, optional): A dictionary to store word counts.
                                  Defaults to {}.
        after (str, optional): A Reddit post identifier for pagination.
                              Defaults to "".
    """

    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    if after is None:
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, word_dict)
