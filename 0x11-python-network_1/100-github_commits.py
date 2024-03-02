#!/usr/bin/python3
""" Github code challenge of helberton"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
          .format(argv[2], argv[1])
    req = requests.get(url)
    n = 0
    for x in req.json():
        if n < 10:
            print("{}: {}".format(x.get("sha"),
                  x.get("commit").get("author").get("name")))
        n += 1
