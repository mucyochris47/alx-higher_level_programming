#!/usr/bin/python3
"""  a Python script that fetches https://alx-intranet.hbtn.io/status """
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        the_page = response.read()
        print('Body response:')
        print('\t- type:', type(the_page))
        print('\t- content:', the_page)
        print('\t- utf8 content:', the_page.decode('utf-8'))
