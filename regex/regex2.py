#!/usr/local/bin/python3
import re


# Certainly! Here are example strings for the remaining four questions:

# Write a regular expression pattern that matches
#  either the word "cat" or "dog" in a case-insensitive manner.

# Example strings:

# "The cat is playful."
# "A Dog barked loudly."
# "Both Cat and Dog are pets."


def match_string(text):
    pattern = re.compile(r'cat|dog', re.IGNORECASE)
    matches = pattern.findall(text)
    for match in matches:
        print(match)

match_string("A Dog barked loudly.")

# match_string("The cat is playful. is cat")
# match_string("Both Cat and Dog are pets.")

 

