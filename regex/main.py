#!/usr/local/bin/python3
"""this is the module"""
# import re
# """
# to match this pattern (415-555-4242) without regex
# we have to do something like this
# """

# # def is_phoneNumber(number):
# #     if number.isdecimal():
# #         return False
# #     for num in range(0, 3):
# #         if not number[num].isdecimal():
# #             return False
# #         if number[3] != '-':
# #             return False
# #     for num in range(4,7):
# #         if not number[num].isdecimal():
# #             return False
# #         if number[7] != '-':
# #            return False
# #     for num in range(8, 12):
# #         if not number[num].isdecimal():
# #            return False
# #     return True
       
# # phone_number = is_phoneNumber('415-555-4242')
# # not_phone_number = is_phoneNumber("thi is a valid phone number 415-555-4242 Mistar Kelly")


# # print(phone_number)
# # print(not_phone_number)

# #we can simplify this long process just by doing this 

# # phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# def find_number(number):
#     # phone_regex2 = re.compile(r'(\(\d{3}\))-(\d{3}-\d{4})')
#     # phone_regex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
#     pattern = re.compile(r'((\d{3}\))-?(\d{6}-\d{4})')
#     found = pattern.search(number)
#     if found:
#         # mo , ma = found.groups()
#         print("string found {}".format(found.group()))
#     else:
#         print("string not found")

# find_number("I'm going somewhere tonight by the  (415)-555-4242")
# find_number("I'm going somewhere tonight by the  415555-4242")

# # batwoman or batman or batman123?

import pydoc

# # if phone_regex.search("moshi is 415-555-4243 a boy "):
# #    print("phone number found")
# # else:
# #     print("phone number not found")

# main_script.py

import kelly

# print(globals())
kelly.hello()
print(f"In the main script, __name__ is {__name__}")
# answer = globals()
for key, value in list(globals().items()):
    # if key.startswith('__'):
        print(key, value)

