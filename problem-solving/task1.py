"""List Sum:
Create a function that takes a list of numbers as input and returns the sum of all the elements in the list.
"""

def list_sum(lists = []):
    sum = 0
    if isinstance(lists, list):
        for i in lists:
            sum += i
        return sum
    else:
        print("not allowed")
    

total = list_sum("ikjoijn")
print(f"The Total is {total}")


