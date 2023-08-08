#!/usr/bin/python3
"""
Returns the number of subscribers (not active users,
total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'MyRedditBot'}
    
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
