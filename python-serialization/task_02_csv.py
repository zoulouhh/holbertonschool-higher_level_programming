#!/usr/bin/env python3
"""This code converts data from a CSV file into a JSON file.
   It's useful for making the data easier to use or
   share between different software or applications."""


import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"file {csv_filename} not found.")
        return False
    except Exception as e:
        print(f"Error : {e}")
        return False