#!/usr/bin/python3
"""url"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as f:
        print(f.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code})
