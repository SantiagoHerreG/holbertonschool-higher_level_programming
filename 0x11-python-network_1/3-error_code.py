#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of
the response"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            body_res = res.read()
            print(body_res.decode())
    except urllib.error.HTTPError as err:
        print("Error code:", err.code)
