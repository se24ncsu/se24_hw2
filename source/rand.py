"""This module generates an array using random numbers"""
import subprocess


def random_array(arr):
    """Random number generator"""
    shuffled_num = None
    for i, _ in enumerate(range(len(arr))):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
