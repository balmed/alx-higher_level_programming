#!/usr/bin/python3
"""takes url and email, sends a POST request and displays the response"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == '__main__':
    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except HTTPError as err:
        print('Error code:', err.code)
