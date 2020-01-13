#!/usr/bin/python3
"""Write a Python script that takes in a string and sends a search
request to the Star Wars API
"""

import requests
import sys

if __name__ == "__main__":

    param = sys.argv[1]
    res = requests.get("https://swapi.co/api/people/" + "?search=" + param)
    try:
        dict_res = res.json()
        if len(dict_res):
            print("Number of results: {}".format(dict_res["count"]))
            for value in dict_res["results"]:
                print(value["name"])
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except:
        print("No result")
