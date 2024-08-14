#!/usr/bin/python3
"""get"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    body = requests.post(url, data={'q': letter})
    contype = body.headers.get('Content-Type')
    try:
        if body.json():
            print(f"[{body.json().get('id')}] {body.json().get('name')}") 
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')

