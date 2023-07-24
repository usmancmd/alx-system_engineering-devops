#!/usr/bin/python3
"""
Returns information for a given employee ID
and export data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open('{}.csv'.format(user.get("id")), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [csv_writer.writerow(
            [user.get("id"),
             user.get("username"),
             item.get("completed"),
             item.get("title")]
            ) for item in todos]
