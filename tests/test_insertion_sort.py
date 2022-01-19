from sorting.insertion_sort import insertion_sort

def test_insertion_sort():

    item_list = [2,1,5,4,3,0]
    
    assert insertion_sort(item_list) == [0, 1, 2, 3, 4, 5]