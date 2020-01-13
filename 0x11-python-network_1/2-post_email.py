#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(email)
    email = email.encode("ascii")
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(url, email) as res:
        body_res = res.read()
        print(body_res.decode())
