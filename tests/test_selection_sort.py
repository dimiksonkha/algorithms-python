from sorting.selection_sort import selection_sort

def test_selection_sort():
    item_list = [2,1,5,4,3,0]

    item_list = selection_sort(item_list)

    assert item_list[0] == 0
    assert item_list[5] == 5
    assert item_list [3] == 3