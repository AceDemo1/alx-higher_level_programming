#!/usr/bin/python3
"""get"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    body = requests.post(url, data={'email': sys.argv[2]})
    print(body.text)
