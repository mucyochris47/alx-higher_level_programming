#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
variable found in the header of the response.
"""
import sys
from urllib.request import Request, urlopen


if __name__ == "__main__":
    command_url = sys.argv[1]
    req = Request(command_url)
    with urlopen(req) as response:
        print(dict(response.headers).get('X-Request-Id'))
