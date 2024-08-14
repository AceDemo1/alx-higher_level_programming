#!/usr/bin/python3
"""get"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    body = requests.get(url, auth=sys.argv[1], sys.argv[2])
    print(f"{body.json().get('id')}")
