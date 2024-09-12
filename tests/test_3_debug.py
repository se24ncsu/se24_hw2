"""Test case 3"""
from source.rand import random_array

def test_rand_is_numeric():
    """Testing if the array contains only numbers."""
    arr = random_array([0]*10)
    assert all(isinstance(x, (int, float)) for x in arr), "Array should contain only numbers."
