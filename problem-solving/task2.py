"""
List Reversal:
Write a program that reverses a given list. For example, if the input is [1, 2, 3, 4], the output should be [4, 3, 2, 1].
"""

def reverse_list(lst=None):
    lst = []
    reverse_lst = []

    for i in lst:
        popd_lst = lst.pop()
        reverse_list.append(popd_lst)
    return popd_lst


reverse_list([1,2,3,4,5])
print(reverse_list)





# names = [1,2,3,4,5]

# pop_item = names.pop()
# pop_item2 = names.pop()
# print(pop_item)
# print(pop_item2)
# # names.reverse()
# # print(names)