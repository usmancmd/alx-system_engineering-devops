#!/usr/bin/python3
"""
Returns information for a given employee ID
and export data in the JSON format..
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": item.get("title"),
                "completed": item.get("completed"),
                "username": user.get("username")
            } for item in requests.get(url + "todos",
                                    params={"userId": user.get("id")}).json()]
            for user in users}, jsonfile)
