#!/usr/bin/python3
"""get"""
import requests


body = requests('https://alx-intranet.hbtn.io/status')
print('Body response:')
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
