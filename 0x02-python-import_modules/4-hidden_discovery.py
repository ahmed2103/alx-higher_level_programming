#!/usr/bin/python3

if __name__ == "__main":
    import hidden_4

    attributes = dir(hidden_4)
    for name in attributes:
        if name[:2] != "__":
            print(name)
