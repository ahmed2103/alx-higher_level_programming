#!/usr/bin/python3
"""
    Python script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    from sys import argv
    from requests import post
    letter = argv[1] if len(argv) > 1 else letter = ''
    payload = {'q': letter}
    res = post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        j = res.json()
        if not j:
            print('No result')
        else:
            print('[{}] {}'.format(j.get('id'), j.get('name')))
    except ValueError:
        print("Not a valid JSON")
