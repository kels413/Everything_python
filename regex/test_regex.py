#!/usr/local/bin/python3
import re
from uuid import uuid4

# <class name> <id> <attribute name> "<attribute value>"

# let me test if i can match this

def match_string(test):
    pattern = re.compile(r'\(^"([A-Za-z0-9]{8}-[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{12})"\)$')
    match = pattern.search(test)
    if match:
        print("found {}".format(match.group()))
    else:
        print("not found")


match_string('("f78b7151-8a2f-4a08-aba5-9a2176756920")')
# number = str(uuid4())

# print(number)

# uuid = 8-4-4-4-12