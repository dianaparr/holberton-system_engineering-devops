#!/usr/bin/python3
""" Module called 1-export_to_CSV """

import csv
import requests
import sys


def main():
    """ This function (using REST API: https://jsonplaceholder.typicode.com/)
        writes and exports data in csv format """
    id_emp = sys.argv[1]
    r_emp = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         id_emp).json()
    name_emp = r_emp.get('name')

    r_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + id_emp).json()

    with open('{}.csv'.format(id_emp), mode='w') as f:
        emp_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in r_tasks:
            emp_writer.writerow([id_emp, name_emp,
                                 task.get('completed'), task.get('title')])

    # print("Done!")

if __name__ == '__main__':
    main()
