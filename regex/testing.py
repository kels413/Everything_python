#!/usr/local/bin/python3

def hello():
    print("hello world")


for k, v in globals().copy().items():
    if k == '__name__':
        k = ''

if __name__ == "__main__":
    hello()