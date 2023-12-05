def append_write(filename="", text=""):
    """Append `text` to `filename` if it exists, or create `filename` if it doesn't.

    Args:
        filename (str): The file to write to or create.
        text (str): The text to append in utf-8 encoding.

    Returns:
        int: Number of characters written to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
