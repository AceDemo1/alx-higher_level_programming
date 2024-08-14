#!/usr/bin/python3
"""get"""
import urllib.request, sys

url = sys.argv[1]
with urllib.request.urlopen(url) as f:
    body = f.read()
    print(f.getheader('X-Request-Id'))
