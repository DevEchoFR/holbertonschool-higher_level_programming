#!/usr/bin/python3
"""
Adds command-line arguments to a list and saves them to a JSON file.
"""

import sys

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except Exception:
    items = []

for arg in sys.argv[1:]:
    items.append(arg)

save_to_json_file(items, filename)
