from sorting.selection_sort import selection_sort

def test_selection_sort():

    item_list = [2,1,5,4,3,0]
    
    assert selection_sort(item_list) == [0, 1, 2, 3, 4, 5]