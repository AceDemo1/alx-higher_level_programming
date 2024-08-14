#!/usr/bin/python3
"""url"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    body = requests.get(url)
    if body.status_code >= 400:
        print(f'Error code: {body.statues_code}')
    else:
        print(body.text)
