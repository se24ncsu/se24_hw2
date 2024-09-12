from sort.hw2_debugging import merge_sort
from sort.rand import random_array

def is_array_numeric(arr):
    """Check if the array contains only numeric values."""
    return all(isinstance(x, (int, float)) for x in arr)

def test_rand_is_numeric():
    self.assertTrue(is_array_numeric(rand), "Array should contain only numbers.")
