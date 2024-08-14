#!/usr/bin/python3
"""commits"""
import requests
import sys


if __name__ == "__main__":
    body = requests.get(f"https://api.github.com/{sys.argv[1]}/{sys.argv[2]}")
    json = body.json()
    for i in json[:10]:
        print(f"{i.get('sha')}: {i.get('commits').get('author').get('name')}")
