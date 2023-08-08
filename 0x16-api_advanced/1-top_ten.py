#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'MyRedditBot'}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for index, post in enumerate(posts[:10], start=1):
            title = post["data"]["title"]
            print(f"{title}")
    else:
        print('None')
