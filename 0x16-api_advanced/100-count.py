#!/usr/bin/python3
"""
Queries the Reddit API,
parses the title of all hot articles,and prints a
sorted count of given keywords (case-insensitive, delimited by spaces
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My Reddit Scraper"}

    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                if word.lower() in title:
                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1

        after = data["data"]["after"]

        if after is None:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return
        else:
            return count_words(subreddit, word_list, after, counts)
    else:
        return
