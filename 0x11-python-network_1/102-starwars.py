#!/usr/bin/python3
"""Write a Python script that takes in a string and sends a search
request to the Star Wars API
"""

import requests
import sys

if __name__ == "__main__":

    movies_dict = {}
    num_res = 0
    param = sys.argv[1]
    url = "https://swapi.co/api/people/" + "?search=" + param
    while True:
        res = requests.get(url)
        try:
            dict_res = res.json()
            if len(dict_res):
                if num_res:
                    pass
                else:
                    print("Number of results: {}".format(dict_res["count"]))
                    num_res += 1
                for value in dict_res["results"]:
                    print(value["name"])
                    for movie in value["films"]:
                        if movie in movies_dict.keys():
                            print("\t{}".format(movies_dict[movie]))
                        else:
                            movie_res = requests.get(movie)
                            print("\t{}".format(movie_res.json()["title"]))
                            movies_dict[movie] = movie_res.json()["title"]
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
        except:
            print("No result")
        if dict_res["next"]:
            url = dict_res["next"]
        else:
            break
