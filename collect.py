#!/usr/bin/env python3

import csv
import requests
import difflib
import sys
from time import sleep
from pprint import pprint

print("repo_name,new_commit_id,new_file_path,previous_commit_id,previous_file_path,commit_date,committer_name,committer_email,subject,message,new_code,previous_code,code_diff")

with open('s1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        try:
            new_url = "https://raw.githubusercontent.com/{0}/{1}/{2}".format(row["repo_name"], row["new_commit_id"], row["new_file_path"])
            previous_url = "https://raw.githubusercontent.com/{0}/{1}/{2}".format(row["repo_name"], row["previous_commit_id"], row["previous_file_path"])
            new_code = requests.get(new_url).text
            previous_code = requests.get(previous_url).text
            row_string = '"{0}",{1},"{2}",{3},"{4}",{5},"{6}","{7}","{8}","{9}","{10}","{11}","'.format(row["repo_name"], row["new_commit_id"], row["new_file_path"], row["previous_commit_id"], row["previous_file_path"], row["commit_date"], row["committer_name"], row["committer_email"], row["subject"], row["message"], new_code.replace("\n", "\\n").replace("\r", "\\n"), previous_code.replace("\n", "\\n").replace("\r", "\\n"))
            print(row_string, end="")
            for line in difflib.unified_diff(previous_code.splitlines(), new_code.splitlines(), fromfile='previous_code', tofile='new_code', lineterm='', n=0):
                if not ( line.startswith('---') or line.startswith('+++') or line.startswith('@@') ):
                    print(line, end="")
            print('"')
            sleep(1)
        except:
            break
