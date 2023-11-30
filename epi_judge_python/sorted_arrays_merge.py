from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    result = []
    array_ptrs = [0 for i in range(len(sorted_arrays))]
    while True:
        min = None
        min_index = None
        for i in range(len(sorted_arrays)):
            if array_ptrs[i] >= len(sorted_arrays[i]):
                continue
            if min == None or sorted_arrays[i][array_ptrs[i]] < min:
                min = sorted_arrays[i][array_ptrs[i]]
                min_index = i
        if min == None:
            break
        result.append(min)
        array_ptrs[min_index] += 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
