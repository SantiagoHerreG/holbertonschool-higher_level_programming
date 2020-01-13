#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of
the response"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code == requests.codes.ok:
            print(res.text)
    else:
        print("Error code:", res.status_code)
