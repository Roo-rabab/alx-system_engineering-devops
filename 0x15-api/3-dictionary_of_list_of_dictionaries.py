#!/usr/bin/python3
"""Python script is designed to sccess a REST API and retrieve information
about the tasks assigned to a specific employee.
+Using what you did in the task #0, extend your Python script to export
data in the JSON format.
+File name must be: todo_all_employees.json
"""

# Imports two modules - requests for making HTTP requests and sys for accessing
#  system-specific parameters and functions.
import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
