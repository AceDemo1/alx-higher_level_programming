#!/usr/bin/python3
"""get"""
import requests


body = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print(f"\t- type: {type(body.text)}")
print(f"\t- content: {body.text}")
