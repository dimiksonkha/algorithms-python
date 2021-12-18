"""
Python implementation of bubble sort
"""

def bubble_sort(item_list):
    n = len(item_list)
    for i in range(n):
        for j in range(n-i-1):
            if item_list[j] > item_list[j+1]:
                temp = item_list[j]
                item_list[j] = item_list[j+1]
                item_list[j+1] = temp
    return item_list            
