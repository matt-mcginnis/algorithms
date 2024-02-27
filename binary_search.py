import math
from typing import List


# Binary Search
def binary_search(haystack: List[int], needle: int):
    result = -1
    low = 0
    high = len(haystack)
    mid = low + math.floor((high - low) / 2)

    while low < high:
        if haystack[mid] == needle:
            result = mid
            break
        elif haystack[mid] < needle:
            low = mid + 1
            mid = low + math.floor((high - low) / 2)
        else:
            high = mid
            mid = low + math.floor((high - low) / 2)

    return result


def test_needle_at_start():
    haystack = [1, 2, 3, 4, 5]
    needle = 1
    expected = 0
    assert binary_search(haystack, needle) == expected


def test_needle_at_end():
    haystack = [1, 2, 3, 4, 5]
    needle = 5
    expected = 4
    assert binary_search(haystack, needle) == expected


def test_needle_in_middle():
    haystack = [1, 2, 3, 4, 5]
    needle = 3
    expected = 2
    assert binary_search(haystack, needle) == expected


def test_needle_not_in_list():
    haystack = [1, 2, 3, 4, 5]
    needle = 6
    expected = -1
    assert binary_search(haystack, needle) == expected


def test_empty_haystack():
    haystack = []
    needle = 1
    expected = -1
    assert binary_search(haystack, needle) == expected


def test_single_element_haystack_found():
    haystack = [1]
    needle = 1
    expected = 0
    assert binary_search(haystack, needle) == expected


def test_single_element_haystack_not_found():
    haystack = [1]
    needle = 2
    expected = -1
    assert binary_search(haystack, needle) == expected
