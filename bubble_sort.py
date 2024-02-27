from typing import List


# Bubble Sort
def bubble_sort(arr: List[int]):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp

    return arr


def test_bubble_sort_unsorted_array():
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort(arr) == expected


def test_bubble_sort_already_sorted_array():
    arr = [11, 12, 22, 25, 34, 64, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort(arr) == expected


def test_bubble_sort_empty_array():
    arr = []
    expected = []
    assert bubble_sort(arr) == expected


def test_bubble_sort_single_element_array():
    arr = [1]
    expected = [1]
    assert bubble_sort(arr) == expected


def test_bubble_sort_all_equal_elements():
    arr = [5, 5, 5, 5, 5]
    expected = [5, 5, 5, 5, 5]
    assert bubble_sort(arr) == expected


def test_bubble_sort_large_random_array():
    from random import randint

    arr = [randint(0, 1000) for _ in range(1000)]
    # Use Python's built-in sort for generating the expected result
    expected = sorted(arr[:])
    assert bubble_sort(arr) == expected
