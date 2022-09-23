#!/usr/bin/python3
"""
script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    res = r.json()
    print(res.get("id"))
