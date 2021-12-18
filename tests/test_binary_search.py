from searching.binary_search import binary_search

def test_binary_search():
    sorted_list = [1,2,3,4,5,6,7,12,13,25,26]
    item = 12

    assert binary_search(sorted_list, item) == 7

    item = -1
    assert binary_search(sorted_list, item) == -1

    item = 27
    assert binary_search(sorted_list, item) == -1

