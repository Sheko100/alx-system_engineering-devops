#!/usr/bin/python3
"""Module that fetches data associated with the employee who is
specified by id and writes the data into a csv file
"""
import csv
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

    file_name = "{}.csv".format(id)

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            row = [id, username, todo['completed'], todo['title']]
            writer.writerow(row)
