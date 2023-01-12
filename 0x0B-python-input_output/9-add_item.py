#!/usr/bin/python3

""" 9-add_item module """


if __name__ == "__main__":

    import sys
    import json
    import os

    f_n = '7-save_to_json_file'
    save_to_json_file = __import__(f_n).save_to_json_file
    f_n = '8-load_from_json_file'
    load_from_json_file = __import__(f_n).load_from_json_file

    input = sys.argv
    to_save = input[1:]
    f_name = "add_item.json"
    if not os.access(f_name, os.R_OK):
        save_to_json_file(to_save, f_name)
        exit()

    j_file = load_from_json_file(f_name)
    j_file.extend(to_save)
    save_to_json_file(j_file, f_name)
