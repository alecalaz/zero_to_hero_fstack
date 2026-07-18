from math_utilities import sum_list_items

def test_sum_list_items_sums_all_items_correctly():
    #AAA
    # Arrange
    list_input = [3,7]
    # ACt
    result = sum_list_items(list_input)

    # Assert
    assert result == 10
