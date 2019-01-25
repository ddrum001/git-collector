#!/usr/bin/env python3

import csv
import requests
import difflib
import sys
from time import sleep
from pprint import pprint

with open('s1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        try:
            new_url = "https://raw.githubusercontent.com/{0}/{1}/{2}".format(row["repo_name"], row["new_commit_id"], row["new_file_path"])
            previous_url = "https://raw.githubusercontent.com/{0}/{1}/{2}".format(row["repo_name"], row["previous_commit_id"], row["previous_file_path"])
            new_code = requests.get(new_url).text
            previous_code = requests.get(previous_url).text
            for line in difflib.unified_diff(previous_code.splitlines(), new_code.splitlines(), fromfile='previous_code', tofile='new_code', lineterm='', n=0):
                if not ( line.startswith('---') or line.startswith('+++') or line.startswith('@@') ):
                    print(line)
            sleep(0.5)
        except:
            break
