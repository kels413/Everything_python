"""List Sum:
Create a function that takes a list of numbers as input and returns the sum of all the elements in the list.
"""

def list_sum(lists = []):
    sum = 0
    for i in lists:
        sum += i
    print(f"sum of the list is == {sum}")


# list_sum([1,2,3,4,5])


