#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    file_name = sys.argv[1] + '.json'
    per_id = int(sys.argv[1])
    rone = requests.get('https://jsonplaceholder.typicode.com/todos')
    rtwo = requests.get('https://jsonplaceholder.typicode.com/users')
    user_info = rtwo.json()
    todos_info = rone.json()
    with open(file_name, mode='w') as json_file:
        info_json = {}
        info_json[str(per_id)] = []
        """loops through and finds the needed id"""
        for x in user_info:
            if per_id == x.get("id"):
                user_name = (x.get("username"))
        for y in todos_info:
            if per_id == y.get("userId"):
                info_json[str(per_id)].append({"task": y.get("title"),
                                               "completed": y.get("completed"),
                                               "username": user_name})
        json.dump(info_json, json_file)
