#!/usr/local/bin/python3
import re

# Develop a regular expression pattern that
# matches a string containing any number of repetitions of 
# the word "apple," followed by the word "pie."


def match_string(text):
   pattern = re.compile(r'apple | pie')
   matches = pattern.findall(text)

   for match in matches