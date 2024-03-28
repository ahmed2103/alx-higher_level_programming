#!/usr/bin/python3
"""
    script that takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    from sys import argv
    import urllib.request
    import urllib.parse
    data = urllib.parse.urlencode({'email': argv[2]}).encode()
    with urllib.request.urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))