#!/usr/bin/python3

import sys
import requests

if __name__ == "__main__":

    repo_name = sys.argv[1]
    user_name = sys.argv[2]

    headers = {"Accept": "application/vnd.github.cloak-preview"}
    res = requests.get("https://api.github.com/repos/{}/{}/commit\
s".format(user_name, repo_name), headers=headers)

    counter = 0
    result = res.json()

    for commit in result:
        print("{}: {}".format(commit["sha"],
                              commit["commit"]["author"]["name"]))
        counter += 1
        if counter == 10:
            break
