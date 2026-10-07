#!/usr/bin/env python3
"""Module that converts CSV data into JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Reads a CSV file and converts its contents into a JSON file ('data.json')."""
    try:
        data_list = []
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
