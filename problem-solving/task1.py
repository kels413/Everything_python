"""List Sum:
Create a function that takes a list of numbers as input and returns the sum of all the elements in the list.
"""

# def list_sum(lists = []):
#     sum = 0
#     if isinstance(lists, list):
#         for i in lists:
#             sum += i
#         return sum
#     else:
#         print("not allowed")
    

# # total = list_sum("ikjoijn")
# total = list_sum([1,2,3,4,5])
# print(f"The Total is {total}")


# ANOTHER WAY OF SOLVING SAME PROBLEM (TIME EFFICIENCY)


def lst_sum(lst=None):
    if lst is None or  not isinstance(lst, list):
        raise ValueError("input must be a list")
    

Total = lst_sum([1,2,4,5,5])
print(To)
