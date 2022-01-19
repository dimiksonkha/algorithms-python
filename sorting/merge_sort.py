"""
Python implementation of merge sort algorithm
Progress:Implementaion not yet completed. Required Testing

"""
def merge(item_list, left, mid, right):
    size_left = mid - left + 1
    size_right = right - mid
    left_list = [None] * size_left
    right_list = [None]* size_right
    
    for i in range(size_left):
      left_list[i] = item_list[left+i]
    
    for j in range(size_right):
      right_list[j] = item_list[mid+i]
    
    arr3 = [None] * (size_left+size_right)
    i = 0
    j = 0
    k = 0

    while i < size_left and j < size_right:
        if left_list[i] < right_list[j]:
            arr3[k] = left_list[i]
            k+=1
            i+=1

        else:
            arr3[k] = right_list[j]
            k+=1
            j+=1

    while i < size_left :
        arr3[k] = left_list[i]
        k+=1
        i+=1

    while j < size_right :
        arr3[k] = right_list[j]
        k+=1
        j+=1

    item_list = arr3       
      
# left = 0 and right = n-1 where n is the length of item_list
def merge_sort(item_list, left, right):
    if left >=right:
      return
    mid = left + (right-left)/2  
    merge_sort(item_list,left,mid)
    merge_sort(item_list,mid+1,right)
    merge(item_list,left,mid,right)
n = 8
item_list = [1,3,4,5,2,6,8,7,9]
merge_sort(item_list,0,n)
for item in item_list:
  print(item)    
