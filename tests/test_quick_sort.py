from sorting.quick_sort import quick_sort

def test_quick_sort():

    item_list = [2,1,5,4,3,0]
    quick_sort(item_list,0,len(item_list)-1)
    assert item_list == [0, 1, 2, 3, 4, 5]