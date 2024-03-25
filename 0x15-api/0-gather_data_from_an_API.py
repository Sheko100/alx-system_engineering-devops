#!/usr/bin/python3
"""Module that fetches data associated with the employee who is
specified by id
"""
import requests
from sys import argv

if __name__ == "__main__" and len(argv) > 1:
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    res = requests.get(url)
    name = res.json()["name"]

    url = "{}/todos".format(url)
    res = requests.get(url)
    todos = res.json()
    count = len(todos)
    done = 0
    completed = []

    for todo in todos:
        if todo["completed"]:
            done = done + 1
            completed.append(todo["title"])
    print("Employee {} is done with tasks({}/{}):".format(name, done, count))

    for task in completed:
        print("\t {}".format(task))
