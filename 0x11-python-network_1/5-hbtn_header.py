#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the
header of the response.
"""

import requests
import sys

if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    print(req.headers['X-Request-Id'])
