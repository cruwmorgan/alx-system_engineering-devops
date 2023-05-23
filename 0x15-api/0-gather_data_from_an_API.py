#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys

    b, c = 0, 0
    per_id = int(sys.argv[1])
    avgt = []

    rone = requests.get('https://jsonplaceholder.typicode.com/todos')
    rtwo = requests.get('https://jsonplaceholder.typicode.com/users')
    print("Employee ", end="")
    user_info = rtwo.json()
    todos_info = rone.json()
    """loops through and finds the needed id"""
    for x in user_info:
        if per_id == x.get("id"):
            print(x.get("name"), end=" is done with tasks")
    for y in todos_info:
        if per_id == y.get("userId"):
            b += 1
            if y.get("completed") is True:
                c += 1
                avgt.append(y.get("title"))
    print("({}/{}):".format(c, b))
    for z in avgt:
        print("\t {}".format(z))
