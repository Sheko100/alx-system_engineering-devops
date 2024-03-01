#!/usr/bin/python3
"""Module that sends a HTTP request to a specific URL using urllib
"""

import urllib.request

if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as res:
        headers = res.headers
        data = res.read()

        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))
