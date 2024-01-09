from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # TODO - you fill in here.
    # for k in reversed(range(len(perm) - 1)):
    #     if perm[k] > perm[k + 1]:
    #         break
    # print(k)
    # for i in reversed(range(k + 1, len(perm))):
    #     if perm[k] > perm[i]:
    #         break
    # print(i)
    # print(perm)
    # perm[k], perm[i] = perm[i], perm[k]
    # print(perm)
    # perm[k+1:] = reversed(perm[k+1:])
    # print(perm)
    k = len(perm) - 2
    while k >= 0 and perm[k] >= perm[k + 1]:
        k -= 1
    if k == -1:
        return []
    i = len(perm) - 1
    while perm[k] >= perm[i]:
        i -= 1
    perm[k], perm[i] = perm[i], perm[k]
    perm[k + 1:] = reversed(perm[k + 1:])
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
