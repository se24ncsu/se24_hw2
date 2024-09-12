from sort.hw2_debugging import merge_sort
from sort.rand import random_array

def test_merge_sort_with_single_element():
    """Test merge_sort with a single-element array."""
    single_element_array = [0]
    sorted_values = merge_sort(single_element_array)
    assert sorted_values == sorted(single_element_array), "Array is not sorted correctly"

def test_merge_sort_with_negative_values():
    """Test merge_sort with an array of negative integers."""
    values = [-i for i in range(1, 11)]
    sorted_values = merge_sort(values)
    assert sorted_values == sorted(values), "Array is not sorted correctly"
