#!/usr/local/bin/python3
"""name"""
# name.py

# def hello():
#     print("Hello from the module!")

# print(f"In main module, __name__ is {__name__}")

print(__file__)

for key, value in globals().copy().items():
    # if key.startswith('__'):
    print(key, value)