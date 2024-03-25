#!/usr/bin/python3
"""Module that fetches data associated with the employee who is
specified by id and writes the data into a json file
"""
import json
import requests
from sys import argv

if __name__ == "__main__" and len(argv) > 1:
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    res = requests.get(url)
    username = res.json()["username"]

    url = "{}/todos".format(url)
    res = requests.get(url)
    todos = res.json()

    file_name = "{}.json".format(id)

    key = str(id)
    user_dct = {key: []}
    for todo in todos:
        todo_dct = {
                'task': todo['title'],
                'completed': todo['completed'],
                'username': username
                }
        user_dct[key].append(todo_dct)

    with open(file_name, 'w', newline='') as json_file:
        json.dump(user_dct, json_file)
