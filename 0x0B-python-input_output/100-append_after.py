#!/usr/bin/python3

""" append_after module """


def append_after(filename="", search_string="", new_string=""):
    """ append_after function """

    with open(filename, mode='r+', encoding='utf-8') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            words = line.split()
            for w in words:
                if search_string in w:
                    lines.insert(idx + 1, new_string)
        f.seek(0)
        f.writelines(lines)
