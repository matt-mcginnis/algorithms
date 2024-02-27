from typing import List


# Linear Search
def linear_search(haystack: List[int], needle: int):
    result = -1
    i = 0
    while i < len(haystack):
        if haystack[i] == needle:
            result = i
            break
        i += 1

    return result


def test_found_single():
    haystack = [1, 2, 3, 4, 5]
    needle = 4
    expected = 3
    assert linear_search(haystack, needle) == expected


def test_found_multiple():
    haystack = [1, 2, 3, 4, 4, 5]
    needle = 4
    expected = 3
    assert linear_search(haystack, needle) == expected


def test_not_found():
    haystack = [1, 2, 3, 4, 5]
    needle = 6
    expected = -1
    assert linear_search(haystack, needle) == expected


def test_empty_haystack():
    haystack = []
    needle = 1
    expected = -1
    assert linear_search(haystack, needle) == expected


def test_different_types():
    haystack = [1, "2", 3, 4, 5]
    needle = 2
    expected = -1  # Function should return -1 since '2' is not the same as 2
    assert linear_search(haystack, needle) == expected
