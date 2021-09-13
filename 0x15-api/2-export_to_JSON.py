#!/usr/bin/python3
""" Module called 2-export_to_JSON """

import json
import requests
import sys


def main():
    """ This function (using REST API: https://jsonplaceholder.typicode.com/)
        writes and exports data in the JSON format """
    id_emp = sys.argv[1]
    r_emp = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         id_emp).json()
    name_emp = r_emp.get('username')

    r_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + id_emp).json()

    data_tasks = dict()
    list_data = list()
    for tasks in r_tasks:
        task_title = tasks.get('title')
        task_status = tasks.get('completed')
        dict_ = {"task": task_title, "completed": task_status,
                 "username": name_emp}
        list_data.append(dict_)
    data_tasks[id_emp] = list_data

    with open('{}.json'.format(id_emp), mode='w') as f:
        json.dump(data_tasks, f)

    # print("Done!")

if __name__ == '__main__':
    main()
