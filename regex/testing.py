#!/usr/local/bin/python3

def hello():
    print("hello world")


for k, v in globals().copy().items():
        print(k, v)


print("this is for testing the globals dictionary")

lists = ["kelly", "okoye", ""]

for i in range(0, 10):
     print(i)

if __name__ == "__main__":
    hello()