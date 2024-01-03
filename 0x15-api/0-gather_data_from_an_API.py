#!/usr/bin/python3
"""Module that gets data from API
"""
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
        todos_dict = todos_res.json()

        name = employee_dict["name"]
        total = len(todos_dict)
        done = 0
        completed = []
        for todo in todos_dict:
            if todo["completed"] is True:
                done = done + 1
                completed.append(todo["title"])

        output = "Employee {} is done with tasks({}/{}):".format(
                name, done, total
                )
        print(output)

        for todo in completed:
            output = "\t {}".format(todo)
            print(output)
