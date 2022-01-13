"""
Python implementation of binary search algorithms
"""

def binary_search(sorted_list, item):
    
    n = len(sorted_list)
    left = 0
    right = n-1 

    mid = (left + right)//2
    item_index = 0
    
    while left <= right:
        
        if item == sorted_list[mid]:
            item_index = mid
            return item_index
        else:
            if item > sorted_list[mid]:
                left = mid +1 
                mid = (left + right)//2
            else:
                right = mid -1
                mid = (left + right)//2
    return -1



