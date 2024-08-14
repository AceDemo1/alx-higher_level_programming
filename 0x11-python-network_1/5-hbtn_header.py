#!/usr/bin/python3
"""get"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    body = requests.get(url)
    print(body.headers.get('X-Request-Id'))
