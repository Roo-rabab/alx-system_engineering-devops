#!/usr/bin/python3
"""
Python script is designed to fetch the number of subscribers for a given
 subreddit from Reddit’s API.
"""

# Import get function which is used to send HTTP requests.
from requests import get


def number_of_subscribers(subreddit):
    """
    defines a function that takes a subreddit name as an argument.
    If an invalid subreddit is given, the function should return 0.
    """

    # checks if the input is None or not a string
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    #  sets the user agent for the HTTP request.
    headers = {'User-agent': 'My browser'}

    # formats the URL to fetch data about the subreddit.
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    # sends a GET request to the URL with the specified user agent.
    response = get(url, headers=headers)

    # converts the response from the GET request into JSON format.
    result = response.json()

    # tries to return the number of subscribers from the JSON data.
    try:
        return result.get('data').get('subscribers')

    # If there’s an error (like the subreddit doesn’t exist), it returns 0.
    except Exception:
        return 0
