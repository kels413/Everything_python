#!/usr/local/bin/python3
# name.py

# def hello():
#     print("Hello from the module!")

# print(f"In main module, __name__ is {__name__}")


for key, value in globals().items():
    # if key.startswith('__'):
    print(key, value)