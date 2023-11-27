#!/usr/bin/python3
"""Python script is designed to sccess a REST API and retrieve information
about the tasks assigned to a specific employee.
+Using what you did in the task #0, extend your Python script to export data
 in the CSV format.
"""


# Imports two modules - requests for making HTTP requests and sys for accessing
#  system-specific parameters and functions.
import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employee_Id

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    with open('{}.csv'.format(employee_Id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_Id, username, task.get('completed'),
                               task.get('title')))
