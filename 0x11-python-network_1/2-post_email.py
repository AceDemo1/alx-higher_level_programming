#!/usr/bin/python3
"""get"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({'email': sys.argv[2]}.encode('utf-8'))2-post_email.py
    with urllib.request.urlopen(url) as f:
        print(f.read().decode('utf-8'))
