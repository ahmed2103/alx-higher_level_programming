def write_file(filename="", text=""):
    with open(filename, 'r', encoding = 'utf-8') as f:
        f.write(text)
        return len(text)

        
