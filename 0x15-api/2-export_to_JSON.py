#!/usr/bin/python3
"""
Returns information for a given employee ID
and export data in the JSON format..
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    with open("{}.json".format(user.get("id")), "w") as jsonfile:
        json.dump({user.get("id"): [{
                "task": item.get("title"),
                "completed": item.get("completed"),
                "username": user.get("id")
             } for item in todos]}, jsonfile)
