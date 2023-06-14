from Challenge27.merge_sort import merge_sort
import pytest

def test_merge_sort():

    # Test case 1: Example
    arr = [8, 4, 23, 42, 16, 15]
    assert merge_sort(arr) == [4, 8, 15, 16, 23, 42]

    # Test case 2: (Reverse-sorted) 
    arr = [20, 18, 12, 8, 5, -2]
    assert merge_sort(arr) == [-2, 5, 8, 12, 18, 20]

    # Test case 3: (Few uniques)
    arr = [5, 12, 7, 5, 5, 7]
    assert merge_sort(arr) == [5, 5, 5, 7, 7, 12]

    # Test case 4: (Nearly-sorted) 
    arr = [2, 3, 5, 7, 13, 11]
    assert merge_sort(arr) == [2, 3, 5, 7, 11, 13]
