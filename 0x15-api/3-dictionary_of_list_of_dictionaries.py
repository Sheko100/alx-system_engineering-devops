#!/usr/bin/python3
"""Module that fetches data associated with all employees who and
writes the data into a json file
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(url)
    users = res.json()

    users_dct = {}

    for user in users:
        id = user['id']
        username = user['username']
        url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

        res = requests.get(url)
        todos = res.json()

        key = str(id)
        users_dct[key] = []
        for todo in todos:
            todo_dct = {
                    'username': username,
                    'task': todo['title'],
                    'completed': todo['completed']
                    }
            users_dct[key].append(todo_dct)

    file_name = "todo_all_employees.json"
    with open(file_name, 'w', newline='') as json_file:
        json.dump(users_dct, json_file)
