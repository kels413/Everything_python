#!/usr/local/bin/python3
# Provide a regular expression pattern to match
# a phone number in the format (XXX) XXX-XXXX, where X represents a digit.

# Example strings:

# "(123) 456-7890"
# "Phone: (987) 654-3210"
# "Invalid: 555-1234"


def is_phoneNumber(text):
   pattern = re.compile(r'(\d{3}) {3}')