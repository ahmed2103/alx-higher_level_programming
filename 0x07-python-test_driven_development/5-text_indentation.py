#!/usr/bin/python3
def text_indentation(text):
    """
    Prints the text with indentation based on punctuation marks such as '?', ':', and '.'

    Args:
    - text (str): The input text to be formatted.

    Raises:
    - TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    beg = 0
    for idx, val in enumerate(text):
        if val in '?:.':
            print(text[beg:idx + 1].strip() + '\n')
            beg = idx + 1
    
    if not beg:  # if no punctuation marks found
        print(text, end='')
    elif beg is not len(text):  # if the loop didn't cover the entire text
        print(text[beg:idx + 1].strip(), end='')
