"""
Python implementation of insertion sort 
"""
def insertion_sort(item_list):
  n = len(item_list)
  for i in range(1,n):
    item = item_list[i]
    j = i-1
    
    while j>=0 and item_list[j]> item:
      item_list[j+1] = item_list[j]
      j-=1

    item_list[j+1] = item
      
  return item_list
