from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    # TODO - you fill in here.
    result = []
    index_a = 0
    index_b = 0
    while index_a < len(A) and index_b < len(B):
        if A[index_a] == B[index_b]:
            if len(result) == 0 or result[-1] != A[index_a]:
                result.append(A[index_a])
            index_a += 1
            index_b += 1
        elif A[index_a] < B[index_b]:
            index_a += 1
        else:
            index_b += 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
