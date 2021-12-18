"""
Python implementation of selection sort algorithm
"""

def selection_sort(item_list):
    n = len(item_list)
    for i in range(n):
        index_min = i 
        for j in range(i+1,n):
            if item_list[j] < item_list[index_min]:
                index_min = j

        if index_min != i:
            temp = item_list[i]
            item_list[i] = item_list[index_min]
            item_list[index_min] = temp        

    return item_list
