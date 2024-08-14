#!/usr/bin/python3
"""get"""
import urllib
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as f:
    body = f.read()
    print('Body reponse:')
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
