#!/usr/bin/python3
"""
Returns information for a given employee ID about his/her TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    task_completed = []
    for task in todos:
        if task.get("completed") is True:
            task_completed.append(task.get("title"))
    print("Employee {} is done with tasks ({}/{}):".format(
        user.get("name"), len(task_completed), len(todos)))
    for i in task_completed:
        print("\t {}".format(i))
