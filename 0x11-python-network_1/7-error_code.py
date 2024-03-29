#!/usr/bin/python3
"""
    script that takes in a URL,
    sends a request to the URL and displays the body of the response.
"""
if __name__ == "__main__":
    from sys import argv
    from requests import get
    r = get(argv[1])
    if r.status_code >= 400:
        print('Error code:', r.status_code)
    else:
        print(r.text)
