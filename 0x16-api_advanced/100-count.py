#!/usr/bin/python3
""" raddit api
Script to count subreddit titles with keywords
"""

import requests
import json


def count_words(subreddit, word_list, after="", count=[]):
    """count all words.
    Args:
    subreddit(str): The subreddit to search.
    word_list(list): The list of words to search for in post titles.
    instances(obj): Key/value pairs of words/counts.
    after(str): The parameter for the next page of the API results.
    count(int): The parameter of results matched thus far.
    """
    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'My browser'})

    if request.status_code == 200:
        results = request.json()

        for topic in (results['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = results['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[i])):
                        a = count[i]
                        count[i] = count[j]
                        count[j] = a
                        a = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = a
            for i in range(len(word_list)):
                if (count[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
        else:
            count_words(subreddit, word_list, after, count)
