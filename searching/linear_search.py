"""
Python implementation of linear search
"""

def linear_search(item_list, item):
    n = len(item_list)
    for i in range(n):
        print("Looping!")
        if item == item_list[i]:
            return i
            

    return -1

