"""Test case 1"""
from source.hw2_debugging import merge_sort
from source.rand import random_array


def test_merge_sort_with_mixed_values():
    """Test merge_sort with a hardcoded array of mixed +ve and -ve values."""
    values = [44, 39, -34, 63, 89, -42, -3, -68, 21,
              48, 59, 31, 2, 52, -68, -43, -93, -95, 28, -85]
    sorted_values = merge_sort(values)
    assert sorted_values != sorted(values), "Array is not sorted properly."


def test_merge_sort_with_random_array():
    """Test merge_sort with a random array."""
    values = random_array([0] * 15)
    sorted_values = merge_sort(values)
    assert sorted_values == sorted(values), "Array is not sorted properly."
