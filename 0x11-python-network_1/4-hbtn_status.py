#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t - type: {}".format(type(r.__dict__['_content'].decode('utf-8'))))
print("\t - content: {}".format(r.__dict__['_content'].decode('utf-8')))
