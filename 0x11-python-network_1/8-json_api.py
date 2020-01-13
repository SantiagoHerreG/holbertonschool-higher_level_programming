#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys

if __name__ == "__main__":

    try:
        param = sys.argv[1]
    except:
        param = ""

    post_param = {"q": param}
    res = requests.post("http://0.0.0.0:5000/search_user", data=post_param)
    try:
        print(res.json()) if len(res.json()) else print("No result")
    except ValueError:
        print("Not a valid JSON")
    except:
        print("No result")
