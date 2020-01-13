#!/usr/bin/python3
"""takes your Github credentials (username and password) and uses the
Github API to display your id
"""

import requests
import sys

if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    res = requests.get("https://api.github.com/user", auth=(user, password))
    try:
        dict_res = res.json()
        if len(dict_res):
            print(dict_res["id"])
    except:
        print("None")
