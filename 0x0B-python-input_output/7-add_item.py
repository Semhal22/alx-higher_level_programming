#!/usr/bin/python3
"""Module that imports save_to_json_file, load_from_json_file"""


import sys
import os
"""Adds all arguments to a Python list and then save them to a file
Pushes an empty list to the file if it doesn't exit
"""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
arguments = sys.argv[1:]
filename = "add_item.json"
content = []
if os.path.exists(filename):
    content = load_from_json_file(filename)
content += arguments
save_to_json_file(content, filename)
