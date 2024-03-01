#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    content = req.text
    print('Body response:\n\t- type: <class \'{}\'>\n\t- content: {}'.format(type(content).__name__, content))
