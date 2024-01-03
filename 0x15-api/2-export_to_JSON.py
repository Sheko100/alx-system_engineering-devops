#!/usr/bin/python3
"""Module that gets data from API
"""
import json
import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) > 1:

        id = int(argv[1])
        employee = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        todos = "{}/todos".format(employee)

        employee_res = requests.get(employee)
        todos_res = requests.get(todos)
        employee_dict = employee_res.json()
        todos_data = todos_res.json()

        file_name = "{}.json".format(id)
        username = employee_dict["username"]
        id_str = str(id)
        todos_dict = {id_str: []}

        with open(file_name, "w") as file:
            for todo in todos_data:
                status = todo["completed"]
                title = todo["title"]
                dct = {
                    "task": title,
                    "completed": status,
                    "username": username
                    }
                todos_dict[id_str].append(dct)

            todos_json = json.dumps(todos_dict)
            file.write(todos_json)
