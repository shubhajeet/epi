from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    # TODO - you fill in here.
    max_reach = 0
    current_index = 0
    while current_index <= max_reach and current_index < len(A):
        max_reach = max(max_reach, current_index + A[current_index])
        current_index += 1
    return max_reach >= len(A) - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
