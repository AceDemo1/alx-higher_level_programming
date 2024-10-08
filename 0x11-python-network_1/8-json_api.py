#!/usr/bin/python3
"""get"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    body = requests.post(url, data={'q': letter})
    try:
        json = body.json()
        if json:
            print(f"[{json.get('id')}] {json.get('name')}")
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
