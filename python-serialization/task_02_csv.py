#!/usr/bin/env python3
"""
Module that converts CSV data to JSON format.

Function:
    convert_csv_to_json(filename)
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Converts CSV file data into JSON format
    and writes it to data.json.

    Returns:
        True if successful
        False if an error occurs
    """
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as csv_file:

            reader = csv.DictReader(csv_file)

            data_list = list(reader)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
