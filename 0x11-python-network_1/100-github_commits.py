#!/usr/bin/python3
"""commits"""
import requests
import sys


if __name__ == "__main__":
    body = requests.get(f"https://api.github.com/repos/
            {sys.argv[2]}/{sys.argv[1]}/commits")
    json = body.json()
    for i in json[:10]:
        print(f"{i.get('sha')}: {i.get('commit').get('author').get('name')}")
