#!/usr/local/bin/python3

def hello():
    print("hello world")


for k, v in globals().items():
    print(k, v)

if __name__ == "__main__":
    hello()