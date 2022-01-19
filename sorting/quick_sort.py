def partition(item_list, low, high):
  pivot = item_list[high]
  i = low-1
  for j in range(low,high):
    if item_list[j] < pivot:
      i+=1
      t = item_list[j]
      item_list[j] = item_list[i]
      item_list[i] = t

  t = item_list[high]
  item_list[high] = item_list[i+1]
  item_list[i+1]  = t
  return i+1

def quick_sort(item_list,low,high):
  if low >= high:
    return
  p = partition(item_list,low,high)
  quick_sort(item_list,low,p-1)
  quick_sort(item_list,p+1,high)
       

