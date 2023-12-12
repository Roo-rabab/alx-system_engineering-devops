#!/usr/bin/python3

"""
Python function that queries the Reddit API and prints the titles of
 the first 10 hot posts listed for a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """
    defines a function called top_ten that takes a single argument:
    the name of a subreddit.
    """
    # checks if the subreddit argument is None or not a string
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    # sets the user agent for the HTTP request
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    # Sets the query parameter limit to 10.
    # It limits the number of posts returned by the Reddit API to 10
    p = {'limit': 10}

    # constructs the URL to fetch data about the subreddit
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    # sends an HTTP GET request to the specified URL using the user agent
    # and query parameters set earlier.
    response = get(url, headers=headers, params=p)

    # converts the response from the GET request into a Python dictionary
    # by parsing the JSON data
    results = response.json()

    # extracts the list of posts (referred to as “children”) from the JSON data
    try:
        my_data = results.get('data').get('children')

    # iterates through the list of posts and prints the title of each post.
        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
