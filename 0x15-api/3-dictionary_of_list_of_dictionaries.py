#!/usr/bin/python3
"""Module that gets data from API
"""
import json
import requests

if __name__ == "__main__":

    root_endpoint = "https://jsonplaceholder.typicode.com/"
    employees_endpoint = "{}users/".format(root_endpoint)
    todos_endpoint = "{}todos/".format(root_endpoint)

    employees_json = requests.get(employees_endpoint)
    todos_json = requests.get(todos_endpoint)
    employees = employees_json.json()
    todos = todos_json.json()

    file_name = "todo_all_employees.json"
    dct_of_ls = {}

    for todo in todos:
        user_id = todo["userId"]
        username = employees[user_id - 1]["username"]
        todos_dict = {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
                }
        if user_id not in dct_of_ls:
            dct_of_ls[user_id] = []
        dct_of_ls[user_id].append(todos_dict)

    with open(file_name, "w") as file:

        todos_json = json.dumps(dct_of_ls)
        file.write(todos_json)
