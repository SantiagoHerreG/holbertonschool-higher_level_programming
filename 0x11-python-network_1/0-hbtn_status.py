#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        body = res.read()
        print("Body response:")        
        print("    - type: " + str(type(body)))
        print("    - content: ", end="")
        print(body)
        print("    - utf8 content: " + res.msg)
