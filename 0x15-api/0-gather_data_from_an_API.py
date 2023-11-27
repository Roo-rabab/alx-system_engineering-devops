#!/usr/bin/python3
"""
Python script is designed to sccess a REST API and retrieve information about
the tasks assigned to a specific employee.
"""

# Imports two modules - requests for making HTTP requests and sys for accessing
#  system-specific parameters and functions.
import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    """ This is the base URL of the API endpoint """
    url = baseUrl + "/" + employee_Id
    """appending the employee ID to the base URL."""
    response = requests.get(url)
    """A GET request is made to the API endpoint to retrieve information about
    the specific employee."""
    Employee_Name = response.json().get('name')
    """The response from the API is parsed as JSON and the employee’s name
    is extracted."""

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    """The response from the API is parsed as JSON and assigned to the variable
    tasks."""
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(Employee_Name, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
