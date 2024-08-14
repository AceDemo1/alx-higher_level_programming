#!/usr/bin/python3
"""get"""
import request


body = request('https://alx-intranet.hbtn.io/status')
print('Body response:')
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
