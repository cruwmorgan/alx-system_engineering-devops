#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import json
    import requests

    file_name = "todo_all_employees.json"
    rone = requests.get('https://jsonplaceholder.typicode.com/todos')
    rtwo = requests.get('https://jsonplaceholder.typicode.com/users')
    user_info = rtwo.json()
    todos_info = rone.json()
    with open(file_name, mode='w') as json_file:
        info_json = {}
        list_all = {}
        """loops through and finds the needed id"""
        for x in user_info:
            user_name = x.get("username")
            per_id = x.get("id")
            a = 0
            for y in todos_info:
                if per_id == y.get("userId"):
                    if a == 0:
                        user = y.get("userId")
                        info_json[user] = []
                        a = 1
                    info_json[user].append({"username": user_name,
                                           "task": y.get("title"),
                                            "completed": y.get("completed")})
            list_all.update(info_json)
        json.dump(list_all, json_file)
