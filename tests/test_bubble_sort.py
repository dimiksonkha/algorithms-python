from sorting.bubble_sort import bubble_sort

def test_bubble_sort():
    
    item_list = [2,4,0,6,8,1,3,5]

    assert bubble_sort(item_list) == [0, 1, 2, 3, 4, 5, 6, 8]
    