#!/usr/local/bin/python3
import re

# question

# Create a regular expression pattern to match
# a sequence of at least three consecutive digits
# in a string.

# example
    #"123abc"
    # "45x789"
    # "abc456def"
    # "1a2b3c"
    # "987654"

def match_string(text):
    pattern = re.compile(r'\d{3}')
    matched = pattern.search(text)
    if matched:
        print("found {}".format(matched.group()))

#call the functions
match_string("123abc")
match_string("45x789")
match_string("abc456def")
match_string("1a2b3c")
match_string("987654")


