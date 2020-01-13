#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
using the package requests
"""
import requests


if __name__ == "__main__":

    res = requests.get("https://intranet.hbtn.io/status")
    print("Body response:\n\t- type: " + str(type(res.text)))
    print("\t- content: " + res.text)
