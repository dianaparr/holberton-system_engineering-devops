#!/usr/bin/python3
""" Module called 0-gather_data_from_an_API """

import requests
import sys


def main():
    """ This function (using REST API: https://jsonplaceholder.typicode.com/)
        returns information about employed for a given ID """
    id_emp = sys.argv[1]
    r_emp = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         id_emp).json()

    r_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + id_emp).json()
    tasks_comp = [task for task in r_tasks if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        r_emp.get('name'), len(tasks_comp), len(r_tasks)))

    for task in r_tasks:
        if task.get('completed') is True:
            print("\t {}".format(task.get('title')))

if __name__ == '__main__':
    main()
