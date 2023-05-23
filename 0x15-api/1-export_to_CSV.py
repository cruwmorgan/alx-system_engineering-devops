#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    per_id = int(sys.argv[1])
    per_id_csv = sys.argv[1] + '.csv'
    avgt = []

    rone = requests.get('https://jsonplaceholder.typicode.com/todos')
    rtwo = requests.get('https://jsonplaceholder.typicode.com/users')
    user_info = rtwo.json()
    todos_info = rone.json()

    with open(per_id_csv, mode='w') as csvfile:
        my_file = csv.writer(csvfile, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL)
        """loops through and finds the needed id"""
        for x in user_info:
            if per_id == x.get("id"):
                user_name = (x.get("username"))
        for y in todos_info:
            if per_id == y.get("userId"):
                my_file.writerow([str(per_id), user_name, y.get("completed"),
                                 y.get("title")])
