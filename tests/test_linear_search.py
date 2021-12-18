from searching.linear_search import linear_search

def test_linear_search():
    item_list = [2,3,4]
    item = 3
    assert linear_search(item_list,item) == 1

    item = 6
    assert linear_search(item_list,item) == -1
    
