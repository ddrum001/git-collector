#!/usr/bin/env python3

import csv
import requests
from time import sleep
import difflib

new_url = ""
previous_url = ""

with open('s1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        new_url = "https://raw.githubusercontent.com/{0}/{1}/{2}".format(row["repo_name"], row["new_commit_id"], row["new_file_path"])
        previous_url = "https://raw.githubusercontent.com/{0}/{1}/{2}".format(row["repo_name"], row["previous_commit_id"], row["previous_file_path"])
        new_code = requests.get(new_url).text
        previous_code = requests.get(previous_url).text
        for line in difflib.unified_diff(previous_code, new_code, fromfile='file1', tofile='file2'):
            print(line)
        line_count += 1
        sleep(0.5)
    print('Processed {0} lines.'.format(line_count))
