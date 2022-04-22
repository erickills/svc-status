#!/bin/python

from subprocess import check_output
from re import search
import csv

cmd = 'systemctl --type=service'
services = check_output(cmd.split()).decode().splitlines()[1:]
status = []

for i in services:
    match = search(r'(^.*)loaded.*(running|exited|failed)',i) # status
    if match:
        status.append(list(match.groups()))

status = sorted(status, key = lambda x: x[1], reverse = True)

with open('/home/eric/projects/svc-status/status-results.csv','w') as file: # change the path where to save the result
    writer = csv.writer(file)
    writer.writerows(status)