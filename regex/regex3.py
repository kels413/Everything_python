#!/usr/local/bin/python3
import re
# Provide a regular expression pattern to match
# a phone number in the format (XXX) XXX-XXXX, where X represents a digit.

# Example strings:
# "(123) 456-7890"
# "Phone: (987) 654-3210"
# "Invalid: 555-1234"

def is_phoneNumber(text):
    pattern = re.compile(r'(\(\d{3}\)) \d{3}-\d{4}')
    match = pattern.search(text)
    if match:
        print("found",match.group())
    else:
        print("not found")
  
    
is_phoneNumber("(123) 456-7890")
is_phoneNumber("Phone: (987) 654-3210")
is_phoneNumber("Invalid: 555-1234")
print("hello world")