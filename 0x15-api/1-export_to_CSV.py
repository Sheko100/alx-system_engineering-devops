#!/usr/bin/python3
"""Module that gets data from API
"""
from sys import argv
import csv
import requests

if __name__ == "__main__":

    if len(argv) > 1:

        id = int(argv[1])
        employee = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        todos = "{}/todos".format(employee)

        employee_res = requests.get(employee)
        todos_res = requests.get(todos)
        employee_dict = employee_res.json()
        todos_dict = todos_res.json()

        file_name = "{}.csv".format(id)
        username = employee_dict["username"]

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for todo in todos_dict:
                state = todo["completed"]
                title = todo["title"]

                row = [id, username, state, title]

                writer.writerow(row)
