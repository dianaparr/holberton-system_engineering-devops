#!/usr/bin/python3
""" Module called 3-dictionary_of_list_of_dictionaries """

import json
import requests
import sys


def main():
    """ This function (using REST API: https://jsonplaceholder.typicode.com/)
        writes and exports data in the JSON format
        (Dictionary of list of dictionaries) """
    r_emp = requests.get('https://jsonplaceholder.typicode.com/users/').json()

    r_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos/').json()

    data_tasks = dict()
    for emp in r_emp:
        list_data = list()
        for tasks in r_tasks:
            if emp.get('id') == tasks.get('userId'):
                name_emp = emp.get('username')
                task_title = tasks.get('title')
                task_status = tasks.get('completed')
                dict_ = {"username": name_emp, "task": task_title,
                         "completed": task_status}
            list_data.append(dict_)
        data_tasks[emp.get('id')] = list_data

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(data_tasks, f)

    # print("Done!")

if __name__ == '__main__':
    main()
