#!/usr/local/bin/python3

def hello():
    print("hello world")


for k, v in globals().copy().items():
        print(k, v)


print("this is for testing the globals dictionary")
names = ["kelly", "okoye", "sinner", "emma"]

for index, name in enumerate(names):
   print(name)


num = 5
num2 = 0

sum = num / num2

if __name__ == "__main__":
    hello()