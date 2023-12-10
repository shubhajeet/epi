from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    # TODO - you fill in here.
    low = 0
    high = len(A)
    while low < high:
        mid = low + (high - low) // 2
        if A[mid] >= k:
            high = mid
        else:
            low = mid + 1
    if low >= len(A):
        return -1
    if A[low] != k:
        return -1
    else:
        return low


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
